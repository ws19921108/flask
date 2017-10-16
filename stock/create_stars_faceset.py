#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


from handle_face import *
from urllib2 import urlopen
from urllib import urlencode
import json
from time import sleep

baseurl = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?'

args = {
    'resource_id': 28266,
    'from_mid': 1,
    'format': 'json',
    'ie': 'utf-8',
    'oe': 'utf-8',
    'query': u'明星',
    'sort_type': 1,
    'pn': 0,
    'rn': 100,
}

while True:
    sleep(0.1)
    res = RemoveAllFace(faceset_token)
    if res != -1:
        print 'remove all face'
        break

outFile = open('star_face.csv','w+')
line = 'name,image_url,face_token\n'
outFile.write(line)
count = 0
for i in range(10):
    args['pn'] = 100*i
    fullurl = baseurl + urlencode(args)
    response = urlopen(fullurl).read()
    data = json.loads(response)
    stars = data['data'][0]['result']
    print len(stars)
    for star in stars:
        while True:
            sleep(0.1)
            face_token = DetectFaceByUrl(star['pic_4n_78'])
            if face_token != False:
                break

        if face_token != '':
            while True:
                sleep(0.1)
                if SetUserID(face_token, star['ename']) == True:
                    break

            while True:
                sleep(0.1)
                res = AddFace(faceset_token, face_token)
                if res != False:
                    break

        line = star['ename'] + ',' + star['pic_4n_78'] + ',' + face_token + '\n'
        outFile.write(line)
        print 'suceese',count
        count += 1
outFile.close()




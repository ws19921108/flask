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
#
# while True:
#     res = RemoveAllFace(faceset_token)
#     if res != -1:
#         print 'remove all face'
#         break

for i in range(50,55):
    print i
    args['pn'] = 100*i
    fullurl = baseurl + urlencode(args)
    response = urlopen(fullurl).read()
    data = json.loads(response)
    stars = data['data'][0]['result']
    for star in stars:
        while True:
            face_token = DetectFaceByUrl(star['pic_4n_78'])
            # print face_token
            if face_token != False:
                break

        if face_token != '':
            while True:
                if SetUserID(face_token, star['ename']) == True:
                    break

            while True:
                res = AddFace(faceset_token, face_token)
                if res != False:
                    break





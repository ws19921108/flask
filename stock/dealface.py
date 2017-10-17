#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json
import requests
from time import sleep

api_key = 'slVt2rQyoO4ocSRGWx1uwsgg-10fnFvB'
api_secret = 'gtqgWcTc-uHMaaxc_DkZ84Q-Phi34LFV'
# faceset_token = '104b81ce9355ddb4285d87fe75c9f765'
faceset_token = '1adf3a340b171024a38efb36a66e05eb'

url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail'
payload = {
    'api_key': api_key,
    'api_secret': api_secret,
    'faceset_token': faceset_token,
}

req = requests.post(url=url, data=payload)
data = json.loads(req.text)
print data['face_count']



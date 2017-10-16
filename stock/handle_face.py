#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json
import requests
from time import sleep


api_key = 'slVt2rQyoO4ocSRGWx1uwsgg-10fnFvB'
api_secret = 'gtqgWcTc-uHMaaxc_DkZ84Q-Phi34LFV'
faceset_token = '104b81ce9355ddb4285d87fe75c9f765'

def CreateFaceSet(outer_id=''):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
    }
    if outer_id != '':
        payload['outer_id'] = outer_id
    req = requests.post(url=url, data=payload)
    data = json.loads(req.text)

    return data['faceset_token']


def GetFaceSets():
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getfacesets'
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
    }
    req = requests.post(url=url,data=payload)
    data = json.loads(req.text)
    print data
    facesets = []

    for faceset in data['facesets']:
        facesets.append(faceset['faceset_token'])
    return  facesets

def DeleteFaceSet(faceset_token):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/delete'
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
        'faceset_token': faceset_token,
    }
    req = requests.post(url=url, data=payload)
    data = json.loads(req.text)
    print data

def RemoveAllFace(faceset_token):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/removeface'
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
        'faceset_token': faceset_token,
        'face_tokens': 'RemoveAllFaceTokens',
    }
    req = requests.post(url=url, data=payload)
    data = json.loads(req.text)
    print data
    return data['face_removed']


def GetDetail(faceset_token):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail'
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
        'faceset_token': faceset_token,
    }
    req = requests.post(url=url, data=payload)
    data = json.loads(req.text)
    # print data
    return data['face_tokens']


def DetectFace(filepath):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    files = {'image_file': open(filepath, 'rb')}
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
    }

    req = requests.post(url=url, files=files, data=payload)
    data = json.loads(req.text)
    face_token = data['faces'][0]['face_token']
    return face_token


def AddFace(faceset_token,face_tokens):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
        'faceset_token': faceset_token,
        'face_tokens': face_tokens
    }
    req = requests.post(url=url, data=payload)
    data = json.loads(req.text)
    return data['face_added']

def PrintAllFaceSets():
    facesets = GetFaceSets()
    for faceset in facesets:
        print faceset
        sleep(1)
        print GetDetail(faceset)


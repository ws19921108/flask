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

def CreateFaceSet(outer_id=''):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
    }
    if outer_id != '':
        payload['outer_id'] = outer_id
    try:
        req = requests.post(url=url, data=payload)
        data = json.loads(req.text)

        return data['faceset_token']
    except:
        return False


def GetFaceSets():
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getfacesets'
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
    }
    try:
        req = requests.post(url=url,data=payload)
        data = json.loads(req.text)
        # print data
        facesets = []

        for faceset in data['facesets']:
            facesets.append(faceset['faceset_token'])
        return  facesets
    except:
        return False

def DeleteFaceSet(faceset_token):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/delete'
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
        'faceset_token': faceset_token,
    }
    try:
        req = requests.post(url=url, data=payload)
        data = json.loads(req.text)
        if 'error_message' in data:
            return data['error_message']
        else:
            return True
    except:
        return False

def RemoveAllFace(faceset_token):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/removeface'
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
        'faceset_token': faceset_token,
        'face_tokens': 'RemoveAllFaceTokens',
    }
    try:
        req = requests.post(url=url, data=payload)
        data = json.loads(req.text)
        return data['face_removed']
    except:
        return -1


def GetDetail(faceset_token):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail'
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
        'faceset_token': faceset_token,
    }
    try:
        req = requests.post(url=url, data=payload)
        data = json.loads(req.text)
        # print data
        return data['face_tokens']
    except:
        return False


def DetectFace(filepath):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    files = {'image_file': open(filepath, 'rb')}
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
    }
    try:
        req = requests.post(url=url, files=files, data=payload)
        data = json.loads(req.text)
        face_token = data['faces'][0]['face_token']
        return face_token
    except:
        return False


def AddFace(faceset_token,face_tokens):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
        'faceset_token': faceset_token,
        'face_tokens': face_tokens
    }
    try:
        req = requests.post(url=url, data=payload)
        data = json.loads(req.text)
        return data['face_added']
    except:
        return False

def DetectFaceByUrl(image_url):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
        'image_url': image_url,
    }
    try:
        req = requests.post(url=url,data=payload)
        data = json.loads(req.text)
        # print data
        if len(data['faces']) == 0:
            face_token = ''
        else:
            face_token = data['faces'][0]['face_token']
        return face_token
    except:
        return False

def SetUserID(face_token,user_id):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/face/setuserid'
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
        'face_token': face_token,
        'user_id':  user_id,
    }
    try:
        req = requests.post(url=url, data=payload)
        data = json.loads(req.text)
        if 'error_message' in data:
            return data['error_message']
        else:
            return True
    except:
        return False


def SearchFace(faceset_token, filepath):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
    files = {'image_file': open(filepath, 'rb')}
    payload = {
        'api_key': api_key,
        'api_secret': api_secret,
        'faceset_token': faceset_token,
    }
    try:
        req = requests.post(url=url, files=files, data=payload)
        data = json.loads(req.text)
        # print data
        user_id = data['results'][0]['user_id']
        confidence = data['results'][0]['confidence']
        return user_id,confidence
    except:
        return False

def PrintAllFaceSets():
    facesets = GetFaceSets()
    for faceset in facesets:
        print faceset
        sleep(1)
        print GetDetail(faceset)

# PrintAllFaceSets()

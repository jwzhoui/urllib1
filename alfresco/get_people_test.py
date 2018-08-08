#coding:utf-8
import urllib2
import sys
import re
import base64
from urlparse import urlparse
import httplib
import json

def get_admin_auth_headers():
    username = 'admin'
    password = '1q2w3e4r!'  #
    Accept = "Accept %s" % 'application/json'
    base64string = base64.encodestring(
        '%s:%s' % (username, password))[:-1]  # 注意哦，这里最后会自动添加一个\n 'and6aG91MToxMjM='  'Basic YWRtaW46MXEydzNlNHIh'
    authheader = "Basic %s" % base64string
    headers = {'Authorization': authheader,
               'Accept': Accept,
               }
    return headers
def get_jwzhou1_auth_headers():
    username = 'jwzhou1'
    password = '123'  #
    Accept = "Accept %s" % 'application/json'
    base64string = base64.encodestring(
        '%s:%s' % (username, password))[:-1]  # 注意哦，这里最后会自动添加一个\n 'and6aG91MToxMjM='  'Basic YWRtaW46MXEydzNlNHIh'
    authheader = "Basic %s" % base64string
    headers = {'Authorization': authheader,
               'Accept': Accept,
               }
    return headers

def get_people_auth_headers(userName = None,password = None):
    if not userName or not password:
        raise Exception('alfresco用户名或密码为空')
    username = userName
    if username == 'admin':
        password = '1q2w3e4r!'  #
    Accept = "Accept %s" % 'application/json'
    Content = ' application/octet-stream'
    base64string = base64.encodestring(
        '%s:%s' % (username, password))[:-1]  # 注意哦，这里最后会自动添加一个\n 'and6aG91MToxMjM='  'Basic YWRtaW46MXEydzNlNHIh'
    authheader = "Basic %s" % base64string
    headers = {'Authorization': authheader,
               'Accept': Accept,
               'Content-Type':Content,
               }
    return headers




# 文件预览地址
def get_node_share_info( nodeId, userName, password):
    id =None
    data = {'nodeId': nodeId}
    headers = get_people_auth_headers(userName=userName, password=password)
    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url = '/alfresco/api/-default-/public/alfresco/versions/1/shared-links'
    url = def_url
    http_conn.request('POST', url, json.dumps(data), headers=headers, )
    handle = http_conn.getresponse()
    thepage = handle.read()
    result = json.loads(thepage)
    if result.has_key('entry'):
        id=result['entry']['id']
    elif result.has_key('error') and result['error']['statusCode'] == 409:
        id = result['error']['errorKey'].split('[')[1][:-1]
    preview = 'http://10.16.117.7:8080/share/s/%s' % id


    return preview



# theurl = 'http://10.16.117.7:8080/alfresco/api/-default-/public/alfresco/versions/1/people/test1123'

# headers = get_admin_auth_headers()
#
http_conn = get_node_share_info('74f01e14-1ddb-47a9-a6fd-905ded844e97', 'isoftstone', 'isoftstone')
print http_conn
# url = '/alfresco/api/-default-/public/alfresco/versions/1/people/test1123'
#
# datas=''
# http_conn.request('GET', url,datas, headers=headers,)
# handle = http_conn.getresponse()
# thepage = handle.read()
# print thepage



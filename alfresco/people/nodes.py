#coding:utf-8
import urllib2
import sys
import re
import base64
from urlparse import urlparse
import httplib
import json
import urllib
from alfresco.get_people_test import *
from alfresco.people.people import *

"""
用admin创建人员
"""
# 在站点根创建文件夹  cm:content 是创建文件      cm:folder 是创建文件夹
def creat_file_in_site(site_id,file_name,nodeType = 'cm:folder'):
    node_parent_id = get_site_base_node(site_id)

    datas = {
              "name": file_name,
              "nodeType": nodeType
            }
    headers = get_jwzhou1_auth_headers()

    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/nodes/'+node_parent_id+'/children'
    url = def_url
    http_conn.request('POST', url, json.dumps(datas), headers=headers, )
    handle = http_conn.getresponse()
    thepage = handle.read()
    return thepage


# 在站点根创建文件夹  cm:content 是创建文件      cm:folder 是创建文件夹
def creat_file_in_file(node_parent_id,file_name,nodeType = 'cm:folder'):

    datas = {
              "name": file_name,
              "nodeType": nodeType
            }
    headers = get_jwzhou1_auth_headers()

    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/nodes/'+node_parent_id+'/children'
    url = def_url
    http_conn.request('POST', url, json.dumps(datas), headers=headers, )
    handle = http_conn.getresponse()
    thepage = handle.read()
    return thepage


#站点目录详情
def site_info_file(site_id):
    node_parent_id = get_site_base_node(site_id)
    headers = get_jwzhou1_auth_headers()
    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/nodes/'+node_parent_id+'/children'
    url = def_url
    http_conn.request('GET', url, None, headers=headers, )
    handle = http_conn.getresponse()
    thepage = handle.read()
    return thepage

#节点目录详情
def node_info_file(node_parent_id):
    headers = get_jwzhou1_auth_headers()

    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/nodes/'+node_parent_id+'/children'
    url = def_url
    http_conn.request('GET', url, None, headers=headers, )
    handle = http_conn.getresponse()
    thepage = handle.read()
    return thepage


# 查看下载详情
def get_download_deatil(file_ids):
    datas = {
              "nodeIds": file_ids
            }
    headers = get_jwzhou1_auth_headers()

    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/downloads'
    url = def_url
    http_conn.request('POST', url, json.dumps(datas), headers=headers, )
    handle = http_conn.getresponse()
    thepage = handle.read()
    detail = json.loads(thepage)
    id = detail['entry']['id']
    get_url = def_url+'/'+id
    http_conn.request('GET', get_url, None, headers=headers, )
    handle2 = http_conn.getresponse()
    thepage2 = handle2.read()
    return thepage2

# 查看下载详情
def download_file(node_id):
    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/nodes/'+node_id+'/content?attachment=true'
    url = def_url
    headers = get_jwzhou1_auth_headers()
    http_conn.request('GET', url, None, headers=headers, )
    handle2 = http_conn.getresponse()
    file_name = dict(handle2.msg)['content-disposition'].split(';')[2].split('\'')[-1]
    file_name_new = url=urllib.unquote(file_name)
    thepage2 = handle2.read()
    with open('/opt/data/data/'+file_name_new, "wb") as code:
        code.write(thepage2)
    # return thepage2


if __name__ == '__main__':
    #站点创建文件夹 u'29a36ad1-e279-4897-8085-76c0ecc2d186'
    # ss = creat_file_in_site('beijingdev','ffilee',nodeType = 'cm:content')
    #文件夹下创建文件夹
    ss = creat_file_in_file('86f6db39-0584-49f8-98f2-c56051a99f40','冲突待解决.txt',nodeType='cm:content')
    #获取站点目录 'attachment; filename="     .png"; filename*=UTF-8\\'\\'%e5%a4%a7%e7%a5%9e%e5%88%86%e5%b8%83%e5%9b%be.png'
    # ss = site_info_file('beijingdev')
    #获节点目录
    # ss = node_info_file('311476c7-f80d-4e19-820c-01f2b8ec0fe0')
    # 查看下载详情  '7d125311-18c6-4677-b7da-f74fd4b07d64',
    # ss = get_download_deatil(['9ea838a6-2810-471d-ba47-e4d5dd52af66'])
    #文件下载 f8040baf-e9f7-4714-bfe2-1df766175335
    # ss = download_file('f8040baf-e9f7-4714-bfe2-1df766175335')
    #上传文件新版本

    print ss









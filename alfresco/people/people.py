#coding:utf-8
import urllib2
import sys
import re
import base64
from urlparse import urlparse
import httplib
import json

from alfresco.get_people_test import *

"""
用admin创建人员
"""

def creat_people(id):
    data = None
    if not data:
        datas = {
                  "id": id,
                  "firstName": id,
                  "lastName": "zhou",
                  "email": id+"@isoftstone.com",
                  "password": "123",
            # "quota":'1024000'
                  # "properties":
                  # {
                  #   "my:property": "The value"
                  # }
                }
    headers = get_admin_auth_headers()

    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    # http_conn = httplib.HTTPConnection('10.16.117.7', '8080')

    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/people'
    url = def_url
    http_conn.request('POST', url, json.dumps(datas), headers=headers, )
    handle = http_conn.getresponse()
    thepage = handle.read()
    print thepage

def creat_group(group_name):

    data = None
    if not data:
        datas = {
                  "id": group_name,
                  "displayName": group_name

                }
    headers = get_admin_auth_headers()

    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    # http_conn = httplib.HTTPConnection('10.16.117.7', '8080')

    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/groups'
    url = def_url
    http_conn.request('POST', url, json.dumps(datas), headers=headers, )
    handle = http_conn.getresponse()
    thepage = handle.read()
    return thepage

def add_to_group(group,id,type):
    data = None
    if not data:
        datas = {
                  "id": id,
                  # "memberType": "GROUP",
                  # "memberType": "PERSON",
                  "memberType": type,
                }
    headers = get_admin_auth_headers()
    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/groups/'+group+'/members'
    url = def_url
    http_conn.request('POST', url, json.dumps(datas), headers=headers, )
    handle = http_conn.getresponse()
    thepage = handle.read()
    return thepage

def get_cmis_service_document(data):
    # if not data:
    #     data = {
    #               "id": "jwzhou6",
    #               "memberType": "PERSON",
    #             }
    headers = get_admin_auth_headers()
    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/cmis/versions/1.1/atom/'
    url = def_url
    http_conn.request('get', url, json.dumps(data), headers=headers, )
    handle = http_conn.getresponse()
    thepage = handle.read()
    print thepage


# 用jezhou1创建站点
def creat_site(data):
    if not data:
        datas = {
            "id": "beijingTest2",
                  "title": "beijingTest2",
                  "description": "北京开测试2",
                  "visibility": "PUBLIC"
                  # "visibility": "PRIVATE"
                }
    headers = get_jwzhou1_auth_headers()

    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/sites'
    url = def_url
    http_conn.request('POST', url, json.dumps(datas), headers=headers, )
    handle = http_conn.getresponse()
    thepage = handle.read()
    return thepage

#获取本系统所有站点判断站点是否存在
def site_not_exit(site_id):
    headers = get_admin_auth_headers()

    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/sites'
    url = def_url
    http_conn.request('GET', url, None, headers=headers, )
    handle = http_conn.getresponse()
    thepage = handle.read()
    thepages = json.loads(thepage)
    entries = thepages['list']['entries']
    for entry in entries:
        site_site_id = entry['entry']['id']
        if site_id == site_site_id:
            print False
            return False
    print True
    return True

#判断组是否存在
def group_not_exit(group_id):
    headers = get_jwzhou1_auth_headers()
    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/groups/'+'GROUP_'+group_id
    url = def_url
    http_conn.request('GET', url, None, headers=headers, )
    handle = http_conn.getresponse()
    return False if handle.status == 200 else True


#判断用户是否存在
def people_not_exit(id):
    headers = get_admin_auth_headers()
    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/people/'+id
    url = def_url
    http_conn.request('GET', url, None, headers=headers, )
    handle = http_conn.getresponse()
    return False if handle.status == 200 else True

#将人或组添加到站点
def add_to_site(site,role,id):
    data = None
    if not data:
        datas = {
                'role' : role,
                  "id": id
                }
    headers = get_jwzhou1_auth_headers()
    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/sites/'+site+'/members'
    url = def_url
    http_conn.request('POST', url, json.dumps(datas), headers=headers, )
    handle = http_conn.getresponse()
    thepage = handle.read()
    return thepage

#将组添加到站点
def add_group_to_site(site,role,group_id):
    data = None
    if not data:
        datas = {
                'group' : {'fullName':'GROUP_'+group_id},
                  "role": role
                }
    headers = get_jwzhou1_auth_headers()
    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/sites/'+site+'/members'
    url = def_url
    http_conn.request('POST', url, json.dumps(datas), headers=headers, )
    handle = http_conn.getresponse()
    thepage = handle.read()
    return thepage

#获取站点详情包含文档节点id 以及人员
def get_site_details(site_id):
    datas = None
    headers = get_jwzhou1_auth_headers()
    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/sites/'+site_id+'?relations=containers%2Cmembers'
    url = def_url
    http_conn.request('GET', url, json.dumps(datas), headers=headers, )
    handle = http_conn.getresponse()
    status = handle.status
    if status == 404:
        raise '空间名查不到或不存在'
    thepage = handle.read()
    return thepage

#获取站点详情包含文档节点id 以及人员
def get_site_base_node(site_id):
    datas = None
    headers = get_jwzhou1_auth_headers()
    http_conn = httplib.HTTPConnection('10.16.117.7', '8080')
    def_url =  '/alfresco/api/-default-/public/alfresco/versions/1/sites/'+site_id+'?relations=containers%2Cmembers'
    url = def_url
    http_conn.request('GET', url, json.dumps(datas), headers=headers, )
    handle = http_conn.getresponse()
    status = handle.status
    if status == 404:
        raise '空间名查不到或不存在'
    thepage = handle.read()
    data = json.loads(thepage)
    doc_id = data['relations']['containers']['list']['entries'][0]['entry']['id']
    return doc_id


if __name__ == '__main__':
    # ss = people_not_exit('jwzou2')
    # ss = creat_people('jwzhou5')
    # ss = group_not_exit('beijing')
    # ss = creat_group('beijingdev')
    # ss = add_to_group('GROUP_beijingdev','jwzhou3','PERSON')
    # site_not_exit('beijing')
    # ss = creat_site('')
    ss = get_site_details('beijingdev')
    ss = add_person_to_site('beijing','SiteConsumer','jwzhou2')
    # ss = add_group_to_site('beijingdev','SiteConsumer','beijingdev')

    print ss









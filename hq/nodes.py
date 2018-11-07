# coding:utf-8
import httplib
import json
import time

import requests
"""
用admin创建人员
"""
# 函数执行时间
def exec_time(func):
    def call_fun(*args, **kwargs):
        start_time = time.time()
        ss = func(*args, **kwargs)
        end_time = time.time()
        print ('执行 %s 用时：%f秒' % (func.func_name,end_time - start_time))
        return ss
    return call_fun


def get_people_auth_headers():
    Accept = "Accept %s" % 'application/json'
    Content = ' application/octet-stream'
    headers = {
        'Accept': Accept,
        'Content-Type': Content,
    }
    return headers


# 文件版本详情
def get_file_versions():
    headers = get_people_auth_headers()
    http_conn = httplib.HTTPConnection('localhost', '64633')
    def_url = '/s/?t=tips&q=花园酒店&stamp=20180913103959221'
    url = def_url
    http_conn.request('GET', url, None, headers=headers, )
    handle = http_conn.getresponse()
    thepage = json.loads(handle.read())
    print thepage


def getURL():
    url = 'http://maps.googleapis.com/maps/api/place/textsearch/json?key=AIzaSyDL2Zs3rtKLDvkZgPL5Cz9tXDwcqbi0Yvo&query=%e4%ba%ba%e6%b0%91%e5%a4%a7%e4%bc%9a%e5%a0%82&language=zh-CN'
    res = requests.get(url, )
    print res.text

getURL()
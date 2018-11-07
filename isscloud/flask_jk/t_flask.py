# coding:utf-8
import sys
import redis
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
import gevent
from gevent import monkey
import time
monkey.patch_all()

DEV = True

REDIS = {
    'host': '118.126.117.140',
    'port': 6379,
}
node = redis.StrictRedis(**REDIS)
search_local = 'http://172.16.23.252:9002'


def consumer_search():
    while True:
        consumer_search_url = node.lpop('list:search')
        if consumer_search_url:
            if DEV:
                node.hset('hash:search', consumer_search_url, '{"1":"1","2":"2"}')
                print consumer_search_url
            else:
                response = requests.request('GET', search_local+consumer_search_url, timeout=20000)
                status = response.status_code
                if status == 200:
                    node.hset('hash:search',consumer_search_url,response.text)
                    print response.text
        else:
            time.sleep(0.32)

def consumer_google():
    while True:
        consumer_search_url = node.lpop('list:google')
        if consumer_search_url:
            if DEV:
                node.hset('hash:google', consumer_search_url, '{"11":"11","12":"12"}')
                print consumer_search_url
            else:
                response = requests.request('GET', 'http://maps.googleapis.com'+consumer_search_url,proxies={'http': '198.11.181.175:9556'},timeout=20000)
                status = response.status_code
                if status == 200:
                    node.hset('hash:google',consumer_search_url,response.text)
                    print response.text
        else:
            time.sleep(0.32)

if __name__ == '__main__':


    gevent.joinall([gevent.spawn(consumer_search),gevent.spawn(consumer_google)])
    print 1


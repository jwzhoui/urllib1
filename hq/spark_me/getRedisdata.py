# coding: utf-8
# import random

import redis
import json

from hq.spark_me import redis_data

REDIS = {
    'host':'118.126.117.140',
    # 'host': 'codis-hotel.haoqiao.com',
    'port':6379,
    # 'port': 30000,
    # 'password':123456,
    # 'max_connections':8,
    # 'db':0
}
node = redis.StrictRedis(**REDIS)


# def init_redis_hset():
#
#     for i in range(1000):
#         vs = [random.randint(0,99999999) for i in range(5)]
#         value = node.hset('1222',str(i),json.dumps(vs))
#     print value
#


def redis_node_resule():
    index = 0
    result = {}
    while (True):
        index_, value = node.hscan('hotel_data_server:country_city_ids', cursor=index, match=None, count=1)
        # index_,value = node.hscan('1222',cursor=index, match=None, count=None)
        for values in value.iteritems():
            country_ids = [values[0]] * len(json.loads(values[1]))
            city_ids = json.loads(values[1])
            city_id_map_country_id = dict(zip(city_ids, country_ids))
            result = dict(result, **city_id_map_country_id)
        index = int(index_)
        if index == 0:
            break
    print json.dumps(result)


def redis_node_data():
    index = 0
    result = []
    while (True):
        index_, value = node.hscan('hotel_data_server:country_city_ids', cursor=index, match=None, count=1)
        for values in value.iteritems():
            city_ids = json.loads(values[1])
            result.append({values[0]: city_ids})
        index = int(index_)
        if index == 0:
            break
    print result


def init_data_to_my_redis():
    data = redis_data.redis_hotel_data_server_country_city_ids
    name = 'hotel_data_server:country_city_ids'
    for datas in data:
        for key, values in datas.iteritems():
            resule = node.hset(name, key, json.dumps(values))
            print resule
if __name__ == '__main__':
    init_data_to_my_redis()
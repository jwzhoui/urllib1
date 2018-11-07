# coding: utf-8
import random

import redis
import json
REDIS={
    'host':'127.0.0.1',
    # 'host':'codis-hotel.haoqiao.com',
    'port':6379,
    # 'port':30000,
    # 'password':123456,
    # 'max_connections':8,
    # 'db':0
}
node = redis.StrictRedis(**REDIS)
def init_redis_hset():

    for i in range(1000):
        vs = [random.randint(0,99999999) for i in range(5)]
        value = node.hset('1222',str(i),json.dumps(vs))
    print value



def redis_node():
    index = 0
    result = {}
    while(True):
        index_,value = node.hscan('1222',cursor=index, match=None, count=None)
        for values in value.iteritems():
            country_ids = [values[0]]*len(json.loads(values[1]))
            city_ids = json.loads(values[1])
            city_id_map_country_id = dict(zip(city_ids,country_ids))
            result = dict(result,**city_id_map_country_id)
        index = int(index_)
        if index == 0:
            break
    print json.dumps(result)

# def redis_pool():
#     TOKEN = '75efcc984b5c41f8ba56280e6774968d'
#     uu = RedisCache.get_data("pastry:token:"+TOKEN)
#     print type(uu),uu

if __name__ == '__main__':
    # init_redis_hset()
    redis_node()
    # redis_pool()
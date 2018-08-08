#coding:utf-8
import redis
import redis_test
# from test.redis_poo import RedisCache
import json
REDIS={
    'host':'10.152.136.51',
    'port':16379,
    # 'password':123456,  {'name':[{'key':'value'},{'key2':'value2'}]}
    # 'max_connections':8,
    'db':1
}
def redis_node():
    node =redis.StrictRedis(**REDIS)
    # node.hset(name=name,key=key,value=value)
    # nod=node.hget(name,key)
    seet='{"catalogy:type:政务协同服务":["beehive/局内公文服务","beehive/工作动态服务","beehive/信息报送服务","beehive/综合管理服务","beehive/调控管理服务","beehive/监督检查服务","beehive/财务管理服务","beehive/流通发展服务","beehive/查询分析服务","beehive/数据查询管理","beehive/政务协同系统设置服务","beehive/政务协同用户管理服务"]}'
    ss=redis_test.SS
    #
    # for shash1 in ss:
    #
    #     for shash2 in shash1:
    #         values = shash1.get(shash2)
    #         for va in values:
    #             for vaa in va:
    #                 vaaa = va.get(vaa)
    #                 oov = node.hset(shash2, vaa, vaaa)
    #                 print oov

    for seets1 in ss:
        values=ss.get(seets1)
        for va in values:
            ov=node.sadd(seets1,va)
            print ov
    # uu = RedisCache().get_data("pastry:token:"+TOKEN)
    #         print nod

# def redis_pool():
#     TOKEN = '75efcc984b5c41f8ba56280e6774968d'
#     uu = RedisCache.get_data("pastry:token:"+TOKEN)
#     print type(uu),uu

if __name__ == '__main__':
    redis_node()
    # redis_pool()
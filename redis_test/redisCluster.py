#coding:utf-8
from rediscluster import StrictRedisCluster
import sys
import redis_settings



def redis_cluster():
    redis_nodes = redis_settings.REDIS_NODES
    password = redis_settings.REDIS_PASSWORD
    kwargs = {'password': password}
    redis_nodes_size=len(redis_nodes)
    try:
        if redis_nodes_size > 1:
            redisconn = StrictRedisCluster(startup_nodes=redis_nodes,**kwargs)
        elif redis_nodes_size==1:
            print 1
        else:
            raise 'redis集群配置错误'
    except Exception,e:
        print "Connect Error!"
        sys.exit(1)

    redisconn.set('name','admin')
    redisconn.set('age',18)
    print "name is: ", redisconn.get('name')
    print "age  is: ", redisconn.get('age')

redis_cluster()
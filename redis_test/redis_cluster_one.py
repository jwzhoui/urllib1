#coding:utf-8
import redis
from rediscluster import StrictRedisCluster
import settings


def operator_status(func):
    '''''get operatoration status
    '''

    def gen_status(*args, **kwargs):
        error, result = None, None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            pass
        return  result

    return gen_status

class RedisCache(object):
    def __init__(self):
        self.redis_nodes = settings.REDIS_NODES
        self.password =settings.REDIS_PASSWORD
        self.max_connections=settings.MAX_CONNECTIONS
        redis_nodes_size = len(self.redis_nodes)

        try:
            if redis_nodes_size > 1:
                kwargs = {'password': self.password}
                self._connection = StrictRedisCluster(max_connections=self.max_connections,
                                                      startup_nodes=self.redis_nodes,
                                                      **kwargs)
            elif redis_nodes_size == 1:
                if not hasattr(RedisCache, 'pool'):
                    RedisCache.create_pool(self)
                self._connection = redis.Redis(connection_pool=RedisCache.pool)
            else:
                raise
        except Exception, e:
            print "redis 链接错误"

    @property
    def connection(self):
        return self._connection

    @staticmethod
    def create_pool(self):

        redis_config = self.redis_nodes[0]
        redis_config['password'] = self.password
        redis_config['max_connections'] = self.max_connections
        RedisCache.pool = redis.ConnectionPool(
                **redis_config
            )
    @operator_status
    def set_data(self, key, value):
        '''''set data with (key, value)
        '''
        return self._connection.set(key, value)

    @operator_status
    def get_data(self, key):
        '''''get data by key
        '''
        return self._connection.get(key)

    @operator_status
    def del_data(self, key):
        '''''delete cache by key
        '''
        return self._connection.delete(key)

    @operator_status
    def lpush_data(self, key,value):
        '''存入 list值 只支持单个
        '''
        return self._connection.lpush(key,value)

    @operator_status
    def rpush_data(self, key, *values):
        '''尾部存入 list值 支持多个
        '''
        return self._connection.rpush(key, *values)

    @operator_status
    def lpush_data(self, key,*values):
        '''list头部插入 list 多值
        '''
        return self._connection.lpush(key,*values)

    @operator_status
    def rpop_data(self, name):
        '''list尾部弹出
        '''
        return self._connection.rpop(name)

    @operator_status
    def lpop_data(self, name):
        '''list头部弹出
        '''
        return self._connection.lpop(name)

    @operator_status
    def lpop_data(self, name):
        '''hash set
        '''
        return self._connection.lpop(name)

if __name__ == '__main__':
  print RedisCache().set_data('Testkey', "Simple Test")
  print RedisCache().get_data('Testkey')
  print RedisCache().del_data('Testkey')
  print RedisCache().get_data('Testkey')
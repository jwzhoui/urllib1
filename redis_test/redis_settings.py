# -*- coding: utf-8 -*-
## redis 集群 配置
PASTRY_TOKEN='pastry:token:'
REDIS_NODES = [
    # {'host': '10.156.129.7', 'port': 8001},
    # {'host': '10.156.129.8', 'port': 8002},
    # {'host': '10.156.129.9', 'port': 8003},
    {'host': '10.16.117.24', 'port': 6379},

]
REDIS_PASSWORD = '123456'
MAX_CONNECTIONS = 8
import redis
from redis.client import StrictRedis

import redis_test
import pickle
from cStringIO import StringIO

from test.redis_poo import RedisCache


def redis_node():
    node =redis.StrictRedis(**redis_test.REDIS)
    TOKEN='f8ac29b615624fb9a4a61647a00e7d0e'
    # UU=node.get(TOKEN)
    user='{"name": "admin", "extra": {"auth_type": "1", "auth_id_card_front": "/uploads/071ba880b0c641a1b35c2fa0d31d06a7/0a798d76-d2bd-55a1-9852-dbd71ab890b8.jpg", "auth_provider": "chinadatapay", "auth_phone": "18682218052", "auth_id_card_expire": "2017-03-16", "login_at": "2017-09-26 17:27:04", "auth_id_card": "370783198607291111", "auth_id_card_back": "/uploads/071ba880b0c641a1b35c2fa0d31d06a7/72eb60c0-3cf7-5018-bf5d-6c20996fc9e4.jpg", "auth_sex": "0", "auth_chinadatapay_message": "\u5f02\u5e38\u60c5\u51b5", "auth_code": "753534", "auth_birthday": "2017-03-16", "auth_status": 2, "auth_chinadatapay_code": "10003", "auth_real_name": "\u6c90\u98ce"}, "created_at": "2017-03-14T03:07:29.000000Z", "opneid": null, "email": "123456789@qq.com", "phone": "15210923893", "source": "", "type": 2, "id": "071ba880b0c641a1b35c2fa0d31d06a7", "target": "admin"}'
    node.set("pastry:kk:"+TOKEN,pickle.dump(node))
    # uu=node.get("pastry:token:"+TOKEN)
    # print type(uu),uu
    # TOKEN = '75efcc984b5c41f8ba56280e6774968d'

    uu = RedisCache().get_data("pastry:kk:"+TOKEN)
    print type(uu),uu

# def redis_pool():
#     TOKEN = '75efcc984b5c41f8ba56280e6774968d'
#     uu = RedisCache.get_data("pastry:token:"+TOKEN)
#     print type(uu),uu

if __name__ == '__main__':
    redis_node()
    # redis_pool()
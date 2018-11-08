# encoding: utf-8
import re

import time

import redis
# -*- coding=utf-8 -*-

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import traceback
reload(sys)
sys.setdefaultencoding('utf-8')

#==邮件发送
__MAIL_CONF = dict()
__MAIL_CONF["smtp_server"] = "smtp.exmail.qq.com"
__MAIL_CONF["user"] = "zhoujianwen@haoqiao.com"
__MAIL_CONF["pwd"] = "Zjw478123552"
__MAIL_CONF["From"] = "zhoujianwen@haoqiao.com"
MAIL_LIST = ['277409155@qq.com']
# 无异常等待时间 单位s
NO_ABNORMAL_WAITING_TIME = 2
#==redis
__REDIS_IP = '118.126.117.140'
__REDIS_PORT = 6379
__ERR_REDIS_KEY_EXPIRE = 'hq_err_hash_code:'


def send_mail_to(subject, message, to_list=MAIL_LIST):
    try:
        smtp_client = smtplib.SMTP(__MAIL_CONF["smtp_server"])
        smtp_client.login(__MAIL_CONF["user"], __MAIL_CONF["pwd"])

        send_msg = MIMEMultipart()
        html_att = MIMEText(message, 'plain', 'utf-8')
        send_msg.attach(html_att)

        send_msg["Accept-Language"] = "zh-CN"
        send_msg["Accept-Charset"] = "ISO-8859-1,utf-8"
        send_msg['Subject'] = Header(subject, 'utf-8')
        send_msg['From'] = __MAIL_CONF["From"]
        send_msg['To'] = ';'.join(to_list)
        send_msg['Cc'] = ''

        smtp_client.sendmail(__MAIL_CONF["From"], to_list, send_msg.as_string())
        smtp_client.close()
        return True
    except:
        print traceback.format_exc()
        return False


class RedisCache(object):
    __instance = None
    _instance = None

    @staticmethod
    def create_pool(self):
        redis_config = self.redis_nodes[0]
        redis_config['password'] = self.password
        redis_config['max_connections'] = self.max_connections
        RedisCache.pool = redis.ConnectionPool(
            **redis_config
        )

    def __new__(cls, *args, **kwargs):

        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        self.redis_nodes = [
            {'host': '118.126.117.140', 'port': 6379},
            # {'host': 'codis-hotel.haoqiao.com', 'port': 30000},
        ]
        self.password = None
        self.max_connections = None
        try:
            if not hasattr(RedisCache, 'pool'):
                RedisCache.create_pool(self)
            self._connection = redis.Redis(connection_pool=RedisCache.pool)

        except Exception, e:
            pass

    @classmethod
    def get_connection(cls):
        """
        #获取链接
        """

        return RedisCache()._connection

# 初始化codis集群
redis_handler = RedisCache.get_connection()
# 逐条获取异常信息
def main():
    while True:
        catch_exception = redis_handler.lpop('not_catch_exception')
        if catch_exception:
            # 获取文件路径字符串 的散列函数
            r = r'File "(.*)", line '
            rls = re.findall(r, catch_exception)
            str_file_path = ''.join(rls)
            hq_err_hash = hash(str_file_path)
            err_redis_key = __ERR_REDIS_KEY_EXPIRE+str(hq_err_hash)
            hq_err_hash_time = redis_handler.get(err_redis_key)
            if not hq_err_hash_time:
                # 布存在hash 发邮件
                if not send_mail_to('未捕获异常告警', catch_exception):
                    print "send_mail_to failed"
                # 存如redis并设置过期时间
                redis_handler.set(err_redis_key, time.time())
                redis_handler.expire(err_redis_key, 200)

        else:
            time.sleep(NO_ABNORMAL_WAITING_TIME)

if __name__ == '__main__':
    main()


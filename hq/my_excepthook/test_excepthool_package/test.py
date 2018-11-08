# encoding: utf-8

import re
import time

from hq.my_excepthook.test_excepthool_package.consum_except import redis_handler, send_mail_to

catch_exception = 'Exception in thread Thread-1:\n \
Traceback (most recent call last):\n \
  File "/usr/lib/python2.7/threading.py", line 801, in __bootstrap_inner\n \
    self.run()\n \
  File "/opt/space/urllib1/hq/my_excepthook/run_type/more_thread/except_code.py", line 18, in run\n \
    1/0\n \
ZeroDivisionError: integer division or modulo by zero\n \
'


r = r'File "(.*)", line '
rls = re.findall(r,catch_exception)
str_file_path = ''.join(rls)
hq_err_hash = hash(str_file_path)
err_redis_key = 'hq_err_hash_code%d:'%hq_err_hash
hq_err_hash_time = redis_handler.get(err_redis_key)
if not hq_err_hash_time:
    # 布存在hash 发邮件
    if not send_mail_to('未捕获异常告警', catch_exception):
        print "send_mail_to failed"
    # 存如redis并设置过期时间
    redis_handler.set(err_redis_key,time.time())
    redis_handler.expire(err_redis_key,200)
# 存在hash 啥也不干

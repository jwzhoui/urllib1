# encoding: utf-8
import sys
import time
import traceback

from multiprocessing import Process

sys.path.append('/opt/space/urllib1/')



def quiet_errors(*args,**kwargs):
    err = ''.join(traceback.format_exception(*args,**kwargs))
    print err
    # RedisCache.inset_exc_to_redis(err)
    from hq.my_excepthook.test_excepthool_package.redis_cache import def_inset_exc_to_redis
    def_inset_exc_to_redis(err)

# 重写系统多进程Process的run方法
# def Process_run(self):
#     try:
#         if self._target:
#             self._target(*self._args, **self._kwargs)
#     except Exception:
#         print '走好巧 多进程 异常捕捉'
#         quiet_errors()
#         raise





#========


# 一般捕捉 定义全局异常捕获
sys.excepthook = quiet_errors
sys.__excepthook__ = quiet_errors
# 多进程捕捉
# Process.run = Process_run





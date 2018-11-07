# encoding: utf-8
import sys
import traceback
from multiprocessing import Process


def quiet_errors(exc_type, exc_value, tracebacks):
    # print exc_type
    # print exc_value
    # print tracebacks
    # print '捕获到了异常'
    err = ''.join(traceback.format_exception(exc_type, exc_value, tracebacks))
    # print 3333, traceback.format_exc()
    sys.stderr.write('未捕获异常' + err + '输出结果')
    # print '未捕获异常'+traceback.format_exc()+'输出结果'
    # sys.stdin


# 重写系统多进程Process的run方法
def Process_run(self):
    try:
        if self._target:
            self._target(*self._args, **self._kwargs)
    except Exception:
        quiet_errors(*sys.exc_info())
        # raise




#=======
def hq_format_exc(limit=None):
    """Like print_exc() but return a string."""
    try:
        etype, value, tb = sys.exc_info()
        print '走到好巧多线程异常捕捉'
        return ''.join(traceback.format_exception(etype, value, tb, limit))
    finally:
        etype = value = tb = None

# 一般捕捉 定义全局异常捕获
sys.excepthook = quiet_errors
sys.__excepthook__ = quiet_errors

# 多进程捕捉
Process.run = Process_run
# 多线程捕捉 重写traceback的format_exc函數
traceback.format_exc = hq_format_exc
# 多协程捕捉




#!/usr/bin/env python
# encoding: utf-8
import hq.my_excepthook.test_excepthool_package
import threading
import time
import sys

sys.path.append('/opt/space/urllib1/')
from hq.my_excepthook.run_type.more_thread.except_code import Qr


def my():
    q = Qr()
    q.start()
b = time.time()
my()
print 'my thread time %f'% (time.time()-b)
# print 3444444445
# time.sleep(1)






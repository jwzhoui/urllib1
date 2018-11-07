#!/usr/bin/env python
# encoding: utf-8

import sys
sys.path.append('/opt/space/urllib1/')
import gevent
from traceback import format_exception

import time
import hq.my_excepthook.test_excepthool_package.hq_excepthook
from hq.my_excepthook.run_type.general.except_code import geventTest

# gevent.spawn(geventTest().func1, 'amap', 3)
# gevent.spawn(geventTest().func1, 'amap', 2)
gevent.spawn(geventTest().func1, 'amap', 1)
print 'end'
time.sleep(4)

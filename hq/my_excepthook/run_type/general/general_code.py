#!/usr/bin/env python
# encoding: utf-8
import sys
import gevent
from traceback import format_exception

import time
import hq.my_excepthook.test_excepthool_package.hq_excepthook
from hq.my_excepthook.run_type.general.except_code import geventTest

# geventTest().func1('amap', 3)
4/0
print 'end'
# time.sleep(4)

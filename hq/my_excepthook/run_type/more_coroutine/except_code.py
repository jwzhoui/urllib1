#!/usr/bin/env python
# encoding: utf-8
import gevent
from gevent import monkey
import time
import hq.my_excepthook.test_excepthool_package.hq_excepthook
monkey.patch_all()


class geventTest(object):
    def func1(self,a='1',b=1):
        # time.sleep(5)
        # time.sleep(2)
        1 / 0
        time.sleep(b)
        print a,b




    def func2(self,c='3',d='4'):
        1/0
        # time.sleep(1)
        print(c+d)

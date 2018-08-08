#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@author: wklken@yeah.net
#@version: a test of decorator
#@date: 20121027
#@desc: just a test


import logging

from time import time

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
is_debug = True

def count_time(is_debug):
    def  handle_fuc(func):
        def  handle_args(*args, **kwargs):
            if is_debug:
                begin = time()
                func(*args, **kwargs)
                logging.debug( "[" + func.__name__ + "] -> " + str(time() - begin) )
            else:
                func(*args, **kwargs)
        return handle_args
    return handle_fuc




def pr(q):
    for i in range(1,1000000):
        i = i * 2
    print "hello world"+q

def test(q):
    pr(q)

@count_time(is_debug)
def test2(q):
    pr(q)

@count_time(False)
def test3(q):
    pr(q)

if __name__ == "__main__":
    test('11')
    test2('22')
    test3('33')
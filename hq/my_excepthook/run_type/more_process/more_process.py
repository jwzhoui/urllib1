#!/usr/bin/env python
# encoding: utf-8
import hq.my_excepthook.test_excepthool_package
import sys

sys.path.append('/opt/space/urllib1/')
import multiprocessing
import time


def worker(interval):
    # try:
        print("work start:{0}".format(time.ctime()));
        1 / 0
        time.sleep(interval)
        print("work end:{0}".format(time.ctime()));
    # except:
    #     print 'z主动捕获'

if __name__ == "__main__":

    # p = multiprocessing.Process(worker, args = (1))
    p = multiprocessing.Process(target = worker, args = (2,))
    p.daemon = True
    p.start()
    time.sleep(11)
    print "end!"
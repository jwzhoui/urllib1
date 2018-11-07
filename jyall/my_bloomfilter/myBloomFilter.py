#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import random

from pybloom import BloomFilter

# 创建一个capacity等于100万，error rate等于0.001的bloomfilter对象
bfilter = BloomFilter(100, error_rate=0.1)
bfilter2 = BloomFilter(100, error_rate=0.001)
bfilter3 = BloomFilter(1000, error_rate=0.0001)

l_bfilter = len(bfilter.bitarray)
l_bfilter2 = len(bfilter2.bitarray)
l_bfilter3 = len(bfilter3.bitarray)
# 添加100个元素
for x in xrange(100):
    bfilter.add(str(x))

# 与nmap文件同步
# bfilter.sync()

# 测试error rate
error_in = 0
print 3 in bfilter
for x in xrange(100, 200):
    if str(x) in bfilter:
        error_in += 1

print "error_rate:%s" % (error_in)

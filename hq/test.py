#!/usr/bin/env python
# -*- coding=utf-8 -*-
import traceback

import settings
import os
import logging
import time
import getpass
import sys
import time

import gevent
from gevent import monkey

from logging.handlers import TimedRotatingFileHandler

from gevent.hub import  get_hub
monkey.patch_all()


# 空日志
class MyLog(object):
    def debug(self, *args, **kwargs):
        pass

    def info(self, *args, **kwargs):
        pass

    def warn(self, *args, **kwargs):
        pass

    def error(self, *args, **kwargs):
        pass


# 本地日志
class Logger(object):
    # 日志类
    logger = None

    # 初始化日志模块
    @classmethod
    def init(cls, log_path, log_level=logging.INFO, log_name=None, lock=False):
        """
        :type log_path: str
        :type log_level: intTimedRotatingFileHandler
        :type lock: bool
        :type log_name: str
        :return: bool
        """
        try:
            # 如果目录不存在，创建目录
            if not os.path.exists(log_path):
                os.mkdir(log_path)
            print 'log_path: ', log_path

            # 日志格式
            formatter = logging.Formatter('[%(asctime)s]--[%(process)d]--[%(levelname)s]--%(message)s')

            # 通用日志
            if log_name is None:
                log_name = 'poi_server.log'
            # logger
            log_full_name = os.path.join(log_path, log_name)
            if lock:
                # 加锁版
                # logger_fh = ConcurrentRotatingFileHandler(log_full_name, "a", 100 * 1024 * 1024, 300)
                pass
            else:
                # 无锁版
                logger_fh = TimedRotatingFileHandler(log_full_name, when='d', encoding='utf-8')

            # 记录日志
            logger_fh.setLevel(log_level)
            logger_fh.setFormatter(formatter)
            cls.logger = logging.getLogger()
            cls.logger.setLevel(log_level)
            cls.logger.addHandler(logger_fh)
            cls.logger.info('%s init successful!' % log_full_name)

            # 性能调优时，故意不记日志
            # cls.logger = MyLog()

            # 返回成功
            return True
        except:
            print traceback.format_exc()
            return False

    @classmethod
    def debug(cls, msg):
        cls.logger.debug(msg)

    @classmethod
    def info(cls, msg):
        cls.logger.info(msg)

    @classmethod
    def error(cls, msg):
        cls.logger.error(msg)

    @classmethod
    def warn(cls, msg):
        cls.logger.warn(msg)

    @classmethod
    def critical(cls, msg):
        cls.logger.critical(msg)


class simple_log(object):
    __instance = None

    def __del__(self):
        print 'shanchu l'

    def __new__(cls,*args,**kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, reload=False):
        print reload
        if reload or not hasattr(self, 'my'):
            self.my = time.time()
            print self.my
        root_directory = settings.LOG_PATH
        # 文件不存在就创建
        if not os.path.exists(root_directory):
            os.makedirs(root_directory)
        current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        path = root_directory + current_date
        try:
            os.mkdir(path)
        except OSError:
            pass
        # user = getpass.getuser()
        self.logger = logging.getLogger()
        self.logger.setLevel(settings.LOG_LEVEL)
        logFile = 'poi_server_info.log'
        formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')
        logHand = logging.FileHandler(path + '/' + logFile, encoding='utf-8')
        logHand.setFormatter(formatter)
        logHand.setLevel(settings.LOG_LEVEL)
        logHandSt = logging.StreamHandler()
        logHandSt.setFormatter(formatter)
        self.logger.addHandler(logHand)
        self.logger.addHandler(logHandSt)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)

    def warn(self, msg):
        self.logger.warn(msg)

    def critical(self, msg):
        self.logger.critical(msg)


# simple_log_instance1 = simple_log()
# simple_log_instance1.my = 'you'
# simple_log_instance2 = simple_log()
# print simple_log_instance2.my

# loop = gevent.get_hub().loop
# t = loop.timer(0.0, 1)
# t.start(simple_log,False )
# print 123
# gevent.sleep(10)



def patch_greenlet(f):
    def inner(*args, **kwargs):
        return gevent.spawn(f, *args, **kwargs)

    return inner


@patch_greenlet
def f():
    simple_log(True)


def timer(after, repeat, f ):
    t = get_hub().loop.timer(after, repeat)
    t.start(f)
    return t


def run():

    print >> 123

run()

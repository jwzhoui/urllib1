# -*- coding:utf-8 -*-
import json
import threading
import traceback

import MySQLdb
import logging
import getpass
import sys
import time
import os
import settings
#pip install MySQL-python

class log(object):
    def __init__(self):
        root_directory = settings.ROOT_DIRECTORY
        # 文件不存在就创建
        if not os.path.exists(root_directory):
            os.makedirs(root_directory)
        current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        path = root_directory + current_date
        try:
            os.mkdir(path)
        except OSError:
            pass

        user = getpass.getuser()
        self.logger = logging.getLogger(user)
        self.logger.setLevel(logging.DEBUG)
        logFile = os.path.basename(sys.argv[0]) + '.log'
        # print(os.path.basename(sys.argv[0]))

        formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s')
        logHand = logging.FileHandler(path + '/' + logFile)
        logHand.setFormatter(formatter)
        logHand.setLevel(logging.INFO)
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


mylog = log()


class SQLiteWraper(object):
    """
    数据库的一个小封装，更好的处理多线程写入
    """
    __instance = None
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self):
        self.lock = threading.RLock()  # 锁

    def get_conn(self):
        conn = MySQLdb.connect(**settings.MYSQL_PROPERTIES)
        return conn

    def conn_close(self, conn=None):
        conn.close()

    def conn_trans(func):
        def connection(self, *args, **kwargs):
            self.lock.acquire()
            conn = self.get_conn()
            kwargs['conn'] = conn
            try:
                rs = func(self, *args, **kwargs)
                return rs
            except Exception, me:
                mylog.error(me.args)
                # print '执行方法错误：%s' %  func.func_name
            finally:
                conn.rollback()
                self.conn_close(conn)
                self.lock.release()

        return connection

    @conn_trans
    def fetchall(self, command="", conn=None):
        cu = conn.cursor()
        lists = []
        try:
            cu.execute(command)
            lists = cu.fetchall()
        except Exception, e:
            print e
            pass
        return list(lists)

    @conn_trans
    def execute(self, command, method_flag=0, conn=None):
        cu = conn.cursor()
        try:
            if not method_flag:
                cu.execute(command)
            else:
                cu.execute(command[0], command[1])
            conn.commit()
        except Exception, e:
            return -1
        return 0

    def code(self, list):
        for i, s in enumerate(list):
            s = '' if s == None else s
            list[i] = str(s)
        return list

    # 插入数据
    @conn_trans
    def insertData(self, table, my_dict, conn=None):
        try:
            cu = conn.cursor()
            cols = ', '.join(self.code(my_dict.keys()))
            values = ','.join(['"' + str(i) + '"' for i in self.code(my_dict.values())])
            values = values.replace('"null"', 'null').replace('"None"', 'null').replace('""', 'null')
            sql = 'insert INTO %s (%s) VALUES (%s)' % (table, cols, values)
            cu.execute(sql)
            conn.commit()
        except Exception, e:
            traceback.print_exc()
            mylog.error(e.message + ' 错误sql: %s ' % sql)


sql_conn = SQLiteWraper()


def get_stat_web_list_request_efficiencys():
    sql = 'SELECT stat_period, stat_date, city_id, req_cost, req_num, req_total_num FROM stat_web_list_request_efficiency;'
    mylog.info('获取stat_web_list_request_efficiencysql： '+sql)
    result = sql_conn.fetchall(command=sql)
    for i,v in enumerate(result):
        result[i] = list(v)
        result[i][1] = str(result[i][1])
    mylog.info('stat_web_list_request_efficiencysql数据： ' + json.dumps(result))


if __name__ == '__main__':
    get_stat_web_list_request_efficiencys()

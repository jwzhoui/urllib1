# coding: utf-8
import os
from multiprocessing import Pool
import sqlite3
import threading
import traceback
import MySQLdb
import multiprocessing


class SQLiteWraper(object):
    """
    数据库的一个小封装，更好的处理多线程写入
    """
    def __init__(self, command='', *args, **kwargs):
        self.lock = threading.RLock()  # 锁
        if command != '':
            conn = self.get_conn()
            cu = conn.cursor()
            cu.execute(command)

    def get_conn(self):
        conn = MySQLdb.connect(
            host='192.168.3.207',
            port=3306,
            user='root',
            passwd='root',
            db='bbzf',
            charset='utf8'
        )
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
            except Exception ,me:
                # mylog.error(me.args)
                print '执行方法错误：%s' %  func.func_name
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
        return lists

    # @conn_trans
    def execute(self, command, method_flag=0, conn=None):
        cu = conn.cursor()
        try:
            if not method_flag:
                cu.execute(command)
            else:
                cu.execute(command[0], command[1])

        except sqlite3.IntegrityError, e:
            # print e　'insert into xiaoqu values( 东城逸墅,东城,工体,塔板结合, 2009)'
            return -1
        except Exception, e:
            print e
            return -2
        return 0
    def code(self,list):
        for i,s in enumerate(list):
            s = '' if s==None else s
            list[i] = str(s)
        return list
    # 插入数据
    @conn_trans
    def insertData(self, table, my_dict,conn=None):
        try:
            cu = conn.cursor()
            cols = ', '.join(self.code(my_dict.keys()))
            values = ','.join(['"'+str(i)+'"' for i in self.code(my_dict.values())])
            values = values.replace('"null"', 'null').replace('"None"','null').replace('""','null')
            sql = 'insert INTO %s (%s) VALUES (%s)' % (table, cols,  values )
            cu.execute(sql)
            conn.commit()
        except sqlite3.IntegrityError, e:
            traceback.print_exc()

class myClass(object):
    def task(self,msg):
        for x in range(msg):
            print 'hello, %s' % x
global i,sw
i = 0
sw = SQLiteWraper()


def get_count():
    sql = 'SELECT count(id) FROM `basic_house_image_info`'
    list = sw.fetchall(sql)
    return long(list[0][0])

def get_max():
    sql = 'SELECT max(id) FROM `basic_house_image_info`'
    return long(sw.fetchall(sql)[0][0])

def get_min():
    sql = 'SELECT min(id) FROM `basic_house_image_info`'
    return long(sw.fetchall(sql)[0][0])

def get_ids():
    sql = 'SELECT id FROM `basic_house_image_info`'
    return sw.fetchall(sql)


def del_bhii_id(id,conn):
    sql = 'DELETE FROM `basic_house_image_info` where id = "%d"' % id
    return sw.execute(sql,conn=conn)



def task(ids,a,b,mydict):
    try:
        conn = sw.get_conn()
        o = 0
        for r in range(a,b+1):
            del_bhii_id(ids[r][0],conn)
            del_count = mydict['del_count']
            mydict['del_count']= del_count+1
            if o>200:
                conn.commit()
                o =0
            print '当前线程id%s 当前id %s===当前删除个数 %s'  %(os.getpid(),r,del_count)

    except Exception,e:
        print e.args
if __name__ == '__main__':
    pool_nu = 2
    pool = Pool(processes=pool_nu)
    count = get_count()
    max = get_max()
    min = 0
    ids = get_ids()
    avg = long(count/pool_nu)
    s = myClass()
    mydict = multiprocessing.Manager().dict()
    mydict['del_count'] = 0
    my_class = s.task
    for x in range(pool_nu):
        a = long(min)
        b = long(min+avg)-1
        if x == pool_nu - 1:
            b = len(ids)-1
        pool.apply_async(task, args=(ids,a,b,mydict),)
        min = b+1
    pool.close()
    pool.join()

    print 'processes done.'
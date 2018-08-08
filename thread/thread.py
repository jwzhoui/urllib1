#coding:utf-8
from multiprocessing import Pool,Queue
import time

def f(q):
    i = q.get()-1
    print '222'
    print(i)
    # q.put(i)
if __name__=='__main__':
    q = Queue(10000,ctx=multiprocessing)
    q.put(10000)
    pool = Pool(processes=5)
    res_list = []
    # for i in range(10):
    pool.apply_async(f, (q))
    #     print ('------:%i'%i)
    #     res_list.append(res)
    pool.close()
    pool.join()

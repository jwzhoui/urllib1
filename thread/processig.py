#coding:utf-8
import multiprocessing
import time
from multiprocessing import Queue
def func(msg,q):
    p = q.get()
    print p
    time.sleep(0)
    # print multiprocessing.current_process().name + '-' + msg
    return multiprocessing.current_process().name + '-' + msg

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=40) # 创建4个进程
    results = []
    q = Queue()
    q.put(10000)
    # ss = q.get()
    for i in xrange(1):
        msg = "hello %d" %(i)
        results.append(pool.apply_async(func, (msg,q )))
    pool.close() # 关闭进程池，表示不能再往进程池中添加进程，需要在join之前调用
    pool.join() # 等待进程池中的所有进程执行完毕
    print ("Sub-process(es) done.")

    for res in results:
        print (res.get())
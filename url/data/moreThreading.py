#coding=utf-8
import threading
from time import ctime,sleep



def music(func):
    q = 0
    for i in range(10):
        q = q + 1
        print "I was listening to %s. %s" %(func,ctime()) +'====='+ str(q)
        sleep(0.2)

# music('wojiushiwo ')
def move(func):
    w=0
    for i in range(10):
        w = w + 1
        print "I was at the %s! %s" %(func,ctime()) +'='+ str(w)
        sleep(0.1)

threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(False)
        t.start()
    t.join()
    print "all over %s" %ctime()
#
# if __name__ == '__main__':
#     p = 0
#     for t in threads:
#         t.start()
#
#     for t in threads:
#         p=p+1
#         print p
#         t.join()
#
#     print "all over %s" % ctime()

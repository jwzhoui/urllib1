import gevent
import time
from gevent import monkey
monkey.patch_all()
class geventTest(object):
    def func1(self,a='1',b='2'):
        # time.sleep(5)
        time.sleep(2)
        print(a+b)



    def func2(self,c='3',d='4'):
        time.sleep(1)
        print(c+d)


print 1
gevent.spawn(geventTest().func1,'11','22')
gevent.spawn(geventTest().func2,'33','44')
print 2


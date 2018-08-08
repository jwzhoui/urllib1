# -*- coding:gbk -*-
'''''内置装饰器'''
class A():
    i = 2
    @staticmethod
    def test_static():
        print "static"
    def test_normal(self):
        print "normal"
        print self
        self.test_static()
    @classmethod
    def test_class(cls):
        print "class", cls
        print cls.test_static()

a = A()
# A.test_static()
# a.test_static()
a.test_normal()
# a.test_class()


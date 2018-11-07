#!/usr/bin/env python
# encoding: utf-8
import threading
import sys
import time

sys.path.append('/opt/space/urllib1/')

class Qr(threading.Thread):
    def wo(self):
        print 456
    def jiu(self):
        print 789

    def run(self):
        time.sleep(2)
        1/0
#!/usr/bin/env python  os.path.dirname(os.path.abspath(__file__))
# encoding: utf-8  
# sys_excepthook.py  
"""Replace the default system exception handler. 
ERROR: Helpful error message 
"""
# Stubs for itertools
import os
import sys

sys.path.append('/opt/space/urllib1/')
import itertools
import sys
################################################################################  
# 异常处理函数
import traceback
import threading
from multiprocessing import Process
from threading import Thread




# Process._bootstrap = Process_bootstrap
# ======
# Thread.start=Thread_start
# Thread.__bootstrap = Thread__bootstrap
# Thread.run = Thread_run
# Thread.__bootstrap_inner = Thread_bootstrap_inner
################################################################################

# print sys.exc_info()
# sys.excepthook(*sys.exc_info())
# 2/0

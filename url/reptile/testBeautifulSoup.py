# -*- coding: utf-8 -*-
import urllib

import time


def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print "%.2f%%"% percent




url=r'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3678062706,1961509322&fm=23&gp=0.jpg'
local='/usr/local/src/'

urllib.urlretrieve(url, local+int(time.time()).__str__()+'.png', callbackfunc)
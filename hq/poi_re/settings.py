# -*- coding: utf-8 -*-
import logging
import os
import sys

DEV = False
# DEV = False
HOST = '0.0.0.0'
PORT = 64690
# 项目log级别
LOG_LEVEL = logging.INFO
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(APP_ROOT, 'log/')

# amap poi搜索配置
AMAP_REQ_BASE_URL = 'http://restapi.amap.com/v3/place/text?'
AMAP_REQ_KEY = '64042a21731983a666f0e680db4c5d22'

if DEV:
    # google poi搜索配置
    GOOGLE_REQ_BASE_URL = 'http://118.126.117.140:9002/maps/api/place/%s/json?'
    GOOGLE_REQ_KEY = 'AIzaSyDL2Zs3rtKLDvkZgPL5Cz9tXDwcqbi0Yvo'
    PROXIES = None

    # 数据库配置
    MYSQL_CONFIGS = {
        'hotel_db': {
            'ip': '47.104.6.77',
            'port': '3306',
            'user': 'root',
            'passwd': 'p@ssw1rd',
            'db': 'jwzhou',
            'enable': '1',
        },
    }
    # 搜索服务配置
    SEARCH_SERVER_IP = '118.126.117.140'
    SEARCH_SERVER_PORT = '9002'
    # redis 相关
    REDIS_NODES = [
        {'host': '118.126.117.140', 'port': 6379},
    ]
    REDIS_PASSWORD = None
    MAX_CONNECTIONS = 32
else:
    # google poi搜索配置
    GOOGLE_REQ_BASE_URL = 'http://maps.googleapis.com/maps/api/place/%s/json?'
    GOOGLE_REQ_KEY = 'AIzaSyDL2Zs3rtKLDvkZgPL5Cz9tXDwcqbi0Yvo'
    PROXIES = {'http': '198.11.181.175:9556'}
    # 数据库配置
    MYSQL_CONFIGS = {
        'hotel_db': {
            'ip': 'mysql-test.haoqiao.com',
            'port': '3306',
            'user': 'hotel_user',
            'passwd': 'Ksolp476B',
            'db': 'hotel_test',
            'enable': '1',
        },
    }
    # 搜索服务配置
    SEARCH_SERVER_IP = 'internal-search-server.haoqiao.com'
    SEARCH_SERVER_PORT = '9001'
    # SEARCH_SERVER_IP='172.16.23.252'
    # SEARCH_SERVER_PORT='9002'
    # redis 相关
    REDIS_NODES = [
        {'host': 'codis-test.haoqiao.com', 'port': 19001},
    ]
    REDIS_PASSWORD = None
    MAX_CONNECTIONS = 32

# poi 缓存时间
POI_STATUS_OK_REDIS_EXPIRE = 60 * 60 * 24
POI_STATUS_FAIL_REDIS_EXPIRE = 60 * 60
# poi缓存key开头
POI_STR_REDIS_KEY_PREFIX = 'poi_search:'

# google poi types 是否没有剔除类型
GOOGLE_RULE_OUT_TYPES = ['administrative_area_level_1', 'country', 'locality', 'lodging']

# ********************************************************
# 1.以下配置为gunicorn配置，名字不能随便改
# ********************************************************
GUNICORN_DAEMON = False
GUNICORN_PROC_NAME = "PoiHandleServer"
GUNICORN_WORKER_CONNECTIONS = 10000
GUNICORN_PIDFILE = 'PoiHandleServer.pid'
GUNICORN_ERRORLOG = "gunicorn_poi_err.log"
GUNICORN_WORKERS = 1
GUNICORN_WORKER_CLASS = "gevent"
GUNICORN_LOGLEVEL = "error"
GUNICORN_DEBUG = False
GUNICORN_TIMEOUT = 900
GUNICORN_X_FORWARDED_FOR_HEADER = 'X-FORWARDED-FOR'

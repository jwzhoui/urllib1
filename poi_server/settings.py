# -*- coding: utf-8 -*-
HOST = '0.0.0.0'
PORT = 64690
LOG_PATH = '/data/hq/log/'

AMAP_TOPIC_NAME = 'Amap_POI_Test'
GOOGLE_TOPIC_NAME = 'Google_POI_Test'

AMAP_REQ_BASE_URL = 'http://restapi.amap.com/v3/place/text?'
AMAP_REQ_KEY = '64042a21731983a666f0e680db4c5d22'

GOOGLE_REQ_BASE_URL = 'http://maps.googleapis.com/maps/api/place/textsearch/json?'
GOOGLE_REQ_KEY = 'AIzaSyDL2Zs3rtKLDvkZgPL5Cz9tXDwcqbi0Yvo'
PROXIES = {'http': '198.11.181.175:9556'}

CODIS_SERVER_HOST = 'codis-test.haoqiao.com'
CODIS_SERVER_PORT = '19001'
CODIS_SERVER_PASSWORD = None
REDIS_POI_SEARCH_HEARD = 'poi_search:'

KAFKA_CLUSTER = 'myhost:9092'
KAFKA_ENABLE_AUTO_COMMIT = False
KAFKA_HEARTBEAT_INTERVAL_MS = 30000
KAFKA_SESSION_TIMEOUT_MS = 50000
KAFKA_KEY_DESERIALIZER = 'org.apache.kafka.common.serialization.StringDeserializer'
KAFKA_VALUE_DESERIALIZER = 'value.deserializervalue.deserializer'

SEARCH_SERVER_IP = 'internal-search-server.haoqiao.com'
SEARCH_SERVER_PORT = '9001'

# 1：等待leader只将记录写入其本地日志
# 0：生产者不会等待来自服务器的任何确认[
# 'all'：等待完整的同步副本集写入记录
KAFKA_ACKS = 0
KAFKA_RETRIES = 0
KAFKA_BATCH_SIZE = 16384
KAFKA_KEY_SERIALIZER = 'org.apache.kafka.common.serialization.StringSerializer'
KAFKA_VALUE_SERIALIZER = 'org.apache.kafka.common.serialization.StringSerializer'

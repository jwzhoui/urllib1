
#coding:utf-8
from kafka import KafkaConsumer
import time
#kafka-test.haoqiao.com:9091
#{'bootstrap_servers': 'myhost:9092', 'group_id': 'G_Google_POI_Test', 'enable_auto_commit': False, 'heartbeat_interval_ms': 30000, 'session_timeout_ms': 50000}

consumer = KafkaConsumer( **{'bootstrap_servers': 'myhost:9092', 'group_id': 'G_Google_POI_Test',  'enable_auto_commit': False,})
consumer.subscribe(topics=('Amap_POI_Test'))

for msg in consumer:
    time.sleep(1)
    print msg.value
print "end"
#coding:utf-8
from kafka import KafkaConsumer
import time
#kafka-test.haoqiao.com:9091
#{'bootstrap_servers': 'myhost:9092', 'group_id': 'G_Google_POI_Test', 'enable_auto_commit': False, 'heartbeat_interval_ms': 30000, 'session_timeout_ms': 50000}

consumer = KafkaConsumer( **{'bootstrap_servers': 'myhost:9092', 'enable_auto_commit': True,})
consumer.subscribe(topics=('Amap_POI_Test'))
consume_msg_list = []
# print 'sleep 10s 准备消费'
# time.sleep(10)
for i in range(10000):
    print i
    records = consumer.poll(max_records=1,timeout_ms=5)
    for key, value in records.items():
        print '消费的数据'+str(value[0].value)
        time.sleep(0.5)
    # consumer.commit_async()

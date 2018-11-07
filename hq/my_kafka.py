# coding:utf-8
from kafka import KafkaConsumer
import time

consumer = KafkaConsumer(bootstrap_servers=['kafka.haoqiao.com:8080'])
consumer.subscribe(topics=('Amap_POI_Test'))
time.sleep(5)
for i in range(10):
    msg = consumer.poll(timeout_ms=5)   #从kafka获取消息
    if len(msg.items())>0:
        print msg
    print msg
    time.sleep(1)
#coding:utf-8
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='myhost:9092')
for _ in range(100):
    s = producer.send('WebServer_OnlineLog_Collect', b'some_message_bytes')
    producer.flush()
    print s.is_done

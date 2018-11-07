#coding:utf-8
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='myhost:9092')
for line in open("spark_kafka_data.txt"):
    print line,
    s = producer.send('WebServer_OnlineLog_Collect', line)
    producer.flush()
    print s.is_done
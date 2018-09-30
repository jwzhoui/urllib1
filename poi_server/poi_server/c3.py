from kafka import KafkaConsumer
import time

#{'bootstrap_servers': 'myhost:9092', 'group_id': 'G_Google_POI_Test', 'enable_auto_commit': False, 'heartbeat_interval_ms': 30000, 'session_timeout_ms': 50000}
consumer = KafkaConsumer( **{'bootstrap_servers': 'myhost:9092', 'group_id': 'G_Google_POI_Test', 'enable_auto_commit': False, 'heartbeat_interval_ms': 30000, 'session_timeout_ms': 50000})
consumer.subscribe(topics=('Google_POI_Test'))
consume_msg_list = []
while True:
    records = consumer.poll(max_records=1,timeout_ms=5)
    for key, value in records.items():
        print value
        # time.sleep(0.5)
    consumer.commit_async()
print consume_msg_list
for msg in consumer:
    time.sleep(1)
    print msg


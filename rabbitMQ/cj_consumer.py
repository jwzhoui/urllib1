#coding:utf-8
import pika
import time
credentials = pika.PlainCredentials('naily', '123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='127.0.0.1',credentials=credentials))

channel = connection.channel()
# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.


channel.queue_declare(queue='task_cde6b298-bf78-3e70-9cb5-4adea6dd589e',durable=True)#队列持久化


def callback(ch, method, properties, body):

    print(ch, method, properties)

    print(" [x] Received %r" % body)
    # time.sleep(1)


channel.basic_consume(callback,
                      queue='task_cde6b298-bf78-3e70-9cb5-4adea6dd589e',
                      no_ack=True
                      )
channel.basic_qos(prefetch_count=1)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
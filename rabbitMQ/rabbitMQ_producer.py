#coding:utf-8
import pika

# 建立一个实例
connection = pika.BlockingConnection(
    # pika.ConnectionParameters('10.30.17.248',5672)  # 默认端口5672，可不写
    pika.ConnectionParameters('127.0.0.1',5672)  # 默认端口5672，可不写
    )
# 声明一个管道，在管道里发消息
channel = connection.channel()
# 在管道里声明queue
channel.queue_declare(queue='hello')
# RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
ms = '000000000000 '
for s in xrange(100,111):

    channel.basic_publish(exchange='',
                          routing_key='hello',  # queue名字
                          body=ms+str(s))  # 消息内容
    print(ms+str(s))
connection.close()  # 队列关闭
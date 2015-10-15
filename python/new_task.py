#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.5.167'))
channel = connection.channel()

channel.queue_declare(queue='task_queue')

for num in range(1,230):
    message = str(num)
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message)
    print " [x] Sent %r" % (message,)

connection.close()
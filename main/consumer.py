import pika

params = pika.URLParameters('amqps://mmbswtkj:86-N4IDgbgw8rOZOsWzJd1tTCA27weth@beaver.rmq.cloudamqp.com/mmbswtkj')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print("Received in admin")
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
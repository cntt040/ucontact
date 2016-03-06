import pika
def on_message(channel, method_frame, header_frame, body):
    print method_frame.delivery_tag
    print body
    print "# Do something here"
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
connection = pika.BlockingConnection(pika.ConnectionParameters('10.60.3.150'))
channel = connection.channel()
channel.basic_consume(on_message, 'promote.referral')
try:
    print "Starting"
    channel.start_consuming()

except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()

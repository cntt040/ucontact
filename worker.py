# from carrot.connection import BrokerConnection
# from carrot.messaging import Consumer
import logging
import datetime
import json
import requests
import pika
import multiprocessing
# from elasticsearch import Elasticsearch

# conn = BrokerConnection(hostname="10.50.1.148", port=5672,
# userid="admin", password="ctadmin")
# # conn = BrokerConnection(hostname="10.60.3.150", port=5672,
# #                         userid="guest", password="guest")
# consumer = Consumer(connection=conn, queue="promote.referral",
# exchange="systems.event", routing_key="newad.new")
#
logging.basicConfig(filename='logs/{}.log'.format(datetime.datetime.now().date()), level=logging.INFO)

def run_worker():
    def on_message(channel, method_frame, header_frame, body):
        # print method_frame.delivery_tag
        # print body
        try:
            # logging.info("{}-{}".format(datetime.datetime.now(), body))
            message_data = json.loads(body.encode())
            if message_data.has_key("is_verified") and bool(message_data["is_verified"]):
                payload = json.dumps({'ad_id': message_data['ad_id'], 'user_id': message_data['account_id']})
                r = requests.post("http://localhost:8000/api/v1/redeem/claim_ad_from_queue",
                                  headers={'Content-Type': 'application/json'}, data=payload)
                logging.info("{} Payload: -->{}".format(datetime.datetime.now(), str(payload)))
        except Exception as e:
            logging.error("{}-{}".format(datetime.datetime.now(), e))
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)


    credentials = pika.PlainCredentials('admin', 'ctadmin')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.50.1.148', credentials=credentials))
    channel = connection.channel()
    channel.basic_consume(on_message, 'promote.referral')
    try:
        print "Worker stared"
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()


if __name__ == '__main__':
    jobs = []
    for i in range(4):
        p = multiprocessing.Process(target=run_worker)
        jobs.append(p)
        p.start()
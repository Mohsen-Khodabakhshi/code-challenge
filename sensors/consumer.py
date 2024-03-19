import json

from rabbit import Rabbit

from processor import Process
from entities import Sensor

rabbit = Rabbit()
processor = Process()


def callback(ch, method, properties, body):
    body = json.loads(body)
    sensor = Sensor(body['name'], body['value'])
    processor.change_sensor_value(sensor)
    processor.cache_sensor_value(sensor)
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":
    rabbit.channel.queue_declare(queue='sensors', durable=True)
    rabbit.channel.basic_consume(queue='sensors',
                                 on_message_callback=callback,
                                 auto_ack=False)
    rabbit.channel.start_consuming()

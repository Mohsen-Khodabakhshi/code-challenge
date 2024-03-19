import json
import redis

from services.rabbit import Rabbit

from services.sensor_processor import Process
from config.reader import rabbit_settings, redis_settings
from entities.sensor import Sensor


rabbit = Rabbit(rabbit_settings.host)
processor = Process(redis.StrictRedis(host=redis_settings.host, port=redis_settings.port, db=redis_settings.db))


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

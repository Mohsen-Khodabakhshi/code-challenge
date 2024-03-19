import json
import random
import time
import pika

from services.rabbit import Rabbit
from entities.sensor import Sensor
from dataclasses import asdict
from config.reader import rabbit_settings

rabbit = Rabbit(rabbit_settings.host)


def send_sensor_value(sensor: Sensor, queue: str = 'sensors', routing_key: str = 'sensors') -> None:
    rabbit.channel.queue_declare(queue=queue, durable=True)

    rabbit.channel.basic_publish(exchange='', routing_key=routing_key, body=json.dumps(asdict(sensor)),
                                 properties=pika.BasicProperties(delivery_mode=2)
                                 )


if __name__ == "__main__":

    while True:
        # send 10 sensor values per second
        for _ in range(10):
            first_sensor_value = random.choice(range(0, 10))
            second_sensor_value = random.choice(range(0, 10))
            third_sensor_value = random.choice(range(0, 10))

            send_sensor_value(Sensor('sensor_1', first_sensor_value))
            send_sensor_value(Sensor('sensor_2', second_sensor_value))
            send_sensor_value(Sensor('sensor_3', third_sensor_value))

        time.sleep(1)

    connection.close()

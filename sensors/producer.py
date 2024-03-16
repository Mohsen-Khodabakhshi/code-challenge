import random
import time

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


def send_sensor_value(value: int, queue: str = 'sensors', routing_key: str = 'sensors') -> None:
    channel.queue_declare(queue=queue, durable=True)

    channel.basic_publish(exchange='', routing_key=routing_key, body=str(value), properties=pika.BasicProperties(
        delivery_mode=2,
    ))


if __name__ == "__main__":

    while True:
        # send 10 sensor values per second
        for _ in range(10):
            random_value = random.choice(range(0, 10))
            send_sensor_value(random_value)
        time.sleep(1)

    connection.close()

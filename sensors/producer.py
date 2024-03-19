import random
import time
import pika

from rabbit import Rabbit

rabbit = Rabbit()


def send_sensor_value(value: int, queue: str = 'sensors', routing_key: str = 'sensors') -> None:
    rabbit.channel.queue_declare(queue, True)

    rabbit.channel.basic_publish(exchange='', routing_key=routing_key, body=str(value), properties=pika.BasicProperties(
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

import pika
from pika.exceptions import AMQPConnectionError


class Rabbit:
    def __init__(self, host: str) -> None:
        while True:
            try:
                connection = pika.BlockingConnection(pika.ConnectionParameters(host))
                self.channel = connection.channel()
                break
            except AMQPConnectionError:
                continue

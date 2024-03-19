from abc import ABC, abstractmethod

import pika


class Rabbit(ABC):
    def __init__(self, host: str = 'localhost') -> None:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = connection.channel()

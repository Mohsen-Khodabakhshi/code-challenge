import redis

from entities.sensor import Sensor

class Process:
    def __init__(self, redis_client: redis.StrictRedis):
        self.client = redis_client

    def cache_sensor_value(self, sensor: Sensor):
        self.client.set(sensor.name, sensor.value)

    @staticmethod
    def change_sensor_value(sensor: Sensor):
        # fake process
        return sensor.value + 1

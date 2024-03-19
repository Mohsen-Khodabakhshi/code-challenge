import redis

from entities import Sensor

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)


class Process:
    @staticmethod
    def cache_sensor_value(sensor: Sensor):
        redis_client.set(sensor.name, sensor.value)

    @staticmethod
    def change_sensor_value(sensor: Sensor):
        # fake process
        return sensor.value + 1

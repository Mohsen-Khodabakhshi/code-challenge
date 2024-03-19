import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


class Process:
    @staticmethod
    def cache_sensor_value(sensor_value: int):
        redis_client.set('sensor', sensor_value)

    @staticmethod
    def change_sensor_value(sensor_value: str):
        # fake process
        sensor_value = int(sensor_value)
        sensor_value += 1
        return sensor_value

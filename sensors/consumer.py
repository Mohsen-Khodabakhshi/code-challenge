import pika
import redis

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


def cache_last_sensor_value(sensor_value: int):
    redis_client.set('sensor', sensor_value)


def some_process(sensor_value: str):
    sensor_value = int(sensor_value)
    sensor_value += 1
    return sensor_value


def callback(ch, method, properties, body):
    sensor_value = some_process(body)
    cache_last_sensor_value(sensor_value)
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":
    channel.queue_declare(queue='sensors', durable=True)

    channel.basic_consume(queue='sensors',
                          on_message_callback=callback,
                          auto_ack=False)

    channel.start_consuming()

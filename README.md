# Code Challenge

### Challenges

* It is better that RabbitMQ consumer get limit of queue messages not all at a time.

### Usge

First run RabbitMQ and Redis services:

``` bash
cd services
docker-compose up --build
```

Then you can run consumer.py and producer.py manually to send fake sensor data to RabbitMQ:
``` bash
pip install -r requirements.txt
cd sensors
python consumer.py # run consumer
python producer.py # run producer
```

At the end you can run FastAPI app to see last sensor value that cached:
``` bash
# make sure you are in base directory
docker build -t my_app:latest .
docker run -d --name my_app -p 8000:8000 my_app:latest
```
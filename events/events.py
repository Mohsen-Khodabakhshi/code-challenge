from fastapi import FastAPI

from config.reader import redis_settings

import redis


async def startup_event_handler(app: FastAPI) -> None:
    app.redis = redis.StrictRedis(host=redis_settings.host, port=redis_settings.port, db=redis_settings.db)

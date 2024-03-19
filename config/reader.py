from pydantic_settings import BaseSettings as PydanticBaseSettings

import os


class BaseSettings(PydanticBaseSettings):
    class Config:
        env_file = ".env"


class RedisSettings(BaseSettings):
    host: str = os.getenv("REDIS_HOST", 'localhost')
    port: int = os.getenv("REDIS_PORT", 6379)
    db: int = os.getenv("REDIS_DB", 0)

    class Config:
        env_prefix = "REDIS_"


redis_settings = RedisSettings()


class RabbitSettings(BaseSettings):
    host: str = os.getenv("RABBIT_HOST", 'localhost')
    port: int = os.getenv("RABBIT_PORT", 5672)

    class Config:
        env_prefix = "RABBIT_"


rabbit_settings = RabbitSettings()

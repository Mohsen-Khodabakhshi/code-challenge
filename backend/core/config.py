from pydantic_settings import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    class Config:
        env_file = ".env"


class RedisSettings(BaseSettings):
    host: str = 'redis'
    port: int = 6379
    db: int = 0

    class Config:
        env_prefix = "REDIS_"


redis_settings = RedisSettings()

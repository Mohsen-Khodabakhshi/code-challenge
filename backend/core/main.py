from fastapi import FastAPI

from core import events

app = FastAPI()


@app.on_event("startup")
async def startup_event() -> None:
    await events.startup_event_handler(app)


@app.get("/")
def retrieve_sensor_value():
    return {"value": app.redis.get('sensor')}

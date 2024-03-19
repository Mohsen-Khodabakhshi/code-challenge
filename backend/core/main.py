from fastapi import FastAPI

from core import events

app = FastAPI()


@app.on_event("startup")
async def startup_event() -> None:
    await events.startup_event_handler(app)


@app.get("/{sensor_id}")
def retrieve_sensor_value(sensor_id: int):
    return {"value": app.redis.get(sensor_id)}

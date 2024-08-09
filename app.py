from fastapi import FastAPI
from redis import from_url
import uvicorn

app = FastAPI()

@app.get("/get")
def get_service():
    return {"status":"success", "message":"Hey ! your first project is built on docker"}

@app.get("/redis")
def insert_redis_data():
    redis_client = from_url(url="redis://redis:alpine", db=0)
    redis_client.set("hemanth1", "enjoy pandagoooo1234")
    return {"status":"success"}


uvicorn.run(app, host="0.0.0.0", port=9090)


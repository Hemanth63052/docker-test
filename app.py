from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/get")
def get_service():
    return {"status":"success", "message":"Hey ! your first project is built on docker"}


uvicorn.run(app, host="0.0.0.0", port=9090)


from fastapi import FastAPI

from src.hello.services.index import run_index

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/index")
def index():
    result = run_index()
    return {"result": result}
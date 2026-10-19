from fastapi import FastAPI

server = FastAPI()


@server.get("/health")
def health():
    return {"status": "ok"}


@server.get("/hello")
def hello():
    return {"Hello world:)"}

from fastapi import FastAPI
from uvicorn import run
from otvetoved_core.presentation import api


app = FastAPI()

app.include_router(api.router)


def main():
    run(
        app=app,
        host="0.0.0.0",
        port=8000,
    )

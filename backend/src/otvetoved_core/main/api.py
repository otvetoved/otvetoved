from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware

from otvetoved_core.infrastructure.config import ConfigProvider
from otvetoved_core.infrastructure.database import DatabaseProvider
from otvetoved_core.presentation import api
from otvetoved_core.presentation.api.schemas.tags_metadata import tags_metadata

app = FastAPI(
    root_path="/api",
    openapi_tags=tags_metadata,
    title="Ответовед REST API",
)

origins = [
    "http://127.0.0.1:8010",
    "http://otvetoved.ru",
    "https://otvetoved.ru",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api.router)


def main():
    container = make_async_container(
        ConfigProvider(),
        DatabaseProvider(),
    )
    setup_dishka(container, app)

    run(
        app=app,
        host="0.0.0.0",
        port=8000,
    )

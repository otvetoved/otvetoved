from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from uvicorn import run

from otvetoved_core.infrastructure.config import ConfigProvider
from otvetoved_core.infrastructure.database import DatabaseProvider
from otvetoved_core.presentation import api
from otvetoved_core.presentation.api.schemas.tags_metadata import tags_metadata

app = FastAPI(
    root_path="/api",
    openapi_tags=tags_metadata,
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

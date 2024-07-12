import asyncio

from dishka import make_async_container, AsyncContainer
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from sqladmin import Admin
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware

from otvetoved_core.infrastructure.config import ConfigProvider
from otvetoved_core.infrastructure.database import DatabaseProvider, DatabaseEngine
from otvetoved_core.presentation import api
from otvetoved_core.presentation.api.schemas.tags_metadata import tags_metadata
from otvetoved_core.presentation import admin


app = FastAPI(
    root_path="/api",
    openapi_tags=tags_metadata,
    title="Ответовед REST API",
)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api.router)


async def include_admin(container: AsyncContainer, app_instance):
    engine = await container.get(DatabaseEngine)
    admin_instance = Admin(app_instance, engine)

    admin_instance.add_view(admin.user.UserView)
    admin_instance.add_view(admin.question.QuestionView)
    admin_instance.add_view(admin.question_answer.QuestionAnswerView)


async def prepare():
    container = make_async_container(
        ConfigProvider(),
        DatabaseProvider(),
    )
    await include_admin(container, app)
    setup_dishka(container, app)


def main():
    asyncio.run(prepare())

    run(
        app=app,
        host="0.0.0.0",
        port=8000,
    )

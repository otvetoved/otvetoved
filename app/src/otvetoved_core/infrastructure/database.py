from typing import Annotated
from di.dependent import Injectable

from sqlalchemy import create_engine, BigInteger
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncAttrs

from config import config


def _create_engine(driver: str, is_async: bool):
    if is_async:
        create = create_async_engine
    else:
        create = create_engine

    engine_ = create(
        'postgresql+{}://{}:{}@{}:{}/{}'.format(
            driver,
            config.postgres_user,
            config.postgres_password,
            config.postgres_host,
            config.postgres_port,
            config.postgres_db
        ),
        echo=config.sqlalchemy_echo,
    )

    return engine_


try:
    engine = _create_engine('psycopg', is_async=True)
except ImportError:
    engine = None

try:
    sync_engine = _create_engine('psycopg2', is_async=False)
except ImportError:
    sync_engine = None


async def inject_database_session():
    async with DatabaseSession(engine, expire_on_commit=False) as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        else:
            await session.commit()


# noinspection PyAbstractClass
class DatabaseSession(AsyncSession, Injectable, call=inject_database_session, scope='request'):
    pass


class RelationalMapper(DeclarativeBase, AsyncAttrs):
    pass


async def on_startup():
    async with engine.begin() as _session:
        # await session.run_sync(Base.metadata.drop_all)
        # await session.run_sync(RelationalMapper.metadata.create_all)
        pass


TelegramIdentifier = Annotated[int, mapped_column(BigInteger())]

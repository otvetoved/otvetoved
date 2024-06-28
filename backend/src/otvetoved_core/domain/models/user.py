from __future__ import annotations

from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from otvetoved_core.infrastructure.relational_entity import (
    BaseRelationalEntity,
)


class User(BaseRelationalEntity):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

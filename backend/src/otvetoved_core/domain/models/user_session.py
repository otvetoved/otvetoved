from __future__ import annotations

import uuid

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID


from otvetoved_core.infrastructure.relational_entity import (
    BaseRelationalEntity,
)


class UserSession(BaseRelationalEntity):
    __tablename__ = "user_session"

    session_token: Mapped[UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4)
    session_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int]

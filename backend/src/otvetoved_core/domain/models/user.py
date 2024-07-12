from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship

from otvetoved_core.infrastructure.relational_entity import (
    BaseRelationalEntity,
)


if TYPE_CHECKING:
    from otvetoved_core.domain.models import QuestionAnswer


class User(BaseRelationalEntity):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    email: Mapped[str] = mapped_column(default="mail@example.com")
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    answers: Mapped[list[QuestionAnswer]] = relationship(lazy="selectin")

    def __str__(self):
        return f"#{self.id} {self.username}"

    @property
    def user_rating(self):
        if len(self.answers) == 0:
            return 0
        total_rate = 0
        for answer in self.answers:
            total_rate += answer.total_rating

        return total_rate / len(self.answers)

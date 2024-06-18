from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from otvetoved_core.domain.models.user import User
from otvetoved_core.infrastructure.relational_entity import (
    BaseRelationalEntity,
)


if TYPE_CHECKING:
    from otvetoved_core.domain.models.tag import (  # noqa: F401
        Tag,
        QuestionTag,
    )


class Question(BaseRelationalEntity):
    __tablename__ = 'question'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_by_user_id: Mapped[int | None] = mapped_column(ForeignKey("user.id"))
    brief: Mapped[str]
    text: Mapped[str]

    tags: Mapped[list[Tag]] = relationship(secondary="QuestionTag.__table__")
    created_by_user: Mapped[User] = relationship()


class QuestionAnswer(BaseRelationalEntity):
    __tablename__ = 'question_answer'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))
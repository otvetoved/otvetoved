from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from otvetoved_core.domain.models.tag import (
    Tag,
    QuestionTag,
)
from otvetoved_core.domain.models.user import User
from otvetoved_core.infrastructure.relational_entity import (
    BaseRelationalEntity,
)


class Question(BaseRelationalEntity):
    __tablename__ = 'question'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_by_user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    brief: Mapped[str]
    text: Mapped[str]
    create_time: Mapped[int]

    tags: Mapped[list[Tag]] = relationship(secondary=QuestionTag.__table__, lazy='selectin')
    created_by_user: Mapped[User] = relationship(lazy='selectin')
    answers: Mapped[list[QuestionAnswer]] = relationship(lazy='selectin')


class QuestionAnswer(BaseRelationalEntity):
    __tablename__ = 'question_answer'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))
    created_by_user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    text: Mapped[str]
    create_time: Mapped[int]

    created_by_user: Mapped[User] = relationship(lazy='selectin')
from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from otvetoved_core.infrastructure.relational_entity import (
    BaseRelationalEntity,
)


class User(BaseRelationalEntity):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    username: Mapped[str]


class QuestionTag(BaseRelationalEntity):
    __tablename__ = "question_tag"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"))


class Question(BaseRelationalEntity):
    __tablename__ = 'question'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_by_user_id: Mapped[int | None] = mapped_column(ForeignKey("user.id"))
    brief: Mapped[str]
    text: Mapped[str]

    tags: Mapped[list[Tag]] = relationship(secondary=QuestionTag.__table__)
    created_by_user: Mapped[User] = relationship()


class QuestionAnswer(BaseRelationalEntity):
    __tablename__ = 'question_answer'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))


class Tag(BaseRelationalEntity):
    __tablename__ = 'tag'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]

from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from otvetoved_core.infrastructure.relational_entity import (
    BaseRelationalEntity,
)


class Tag(BaseRelationalEntity):
    __tablename__ = 'tag'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]


class QuestionTag(BaseRelationalEntity):
    __tablename__ = "question_tag"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"))

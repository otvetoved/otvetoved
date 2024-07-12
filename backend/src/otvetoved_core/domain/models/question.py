from __future__ import annotations

from collections import Counter
from datetime import datetime

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
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    tags: Mapped[list[Tag]] = relationship(secondary=QuestionTag.__table__, lazy='selectin')
    created_by_user: Mapped[User] = relationship(lazy='selectin')
    answers: Mapped[list[QuestionAnswer]] = relationship(lazy='selectin', back_populates="question")

    def __str__(self):
        return f"#{self.id} {self.brief}"


class UserAction(BaseRelationalEntity):
    __tablename__ = 'user_answer'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    answer_id: Mapped[int] = mapped_column(ForeignKey("question_answer.id"))
    action: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)


class QuestionAnswer(BaseRelationalEntity):
    __tablename__ = 'question_answer'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))
    created_by_user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    text: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    rating: Mapped[list[UserAction]] = relationship(lazy="selectin")

    created_by_user: Mapped[User] = relationship(lazy='selectin')
    question: Mapped[Question] = relationship(lazy="selectin", back_populates="answers")

    @property
    def likes(self):
        return Counter(i.action for i in self.rating)[True]

    @property
    def dislikes(self):
        return Counter(i.action for i in self.rating)[False]

    @property
    def total_rating(self):
        return self.likes - self.dislikes

from typing import Annotated

from fastapi import APIRouter, HTTPException
from pydantic import Field, UUID4
from dishka.integrations.fastapi import inject, FromDishka
from sqlalchemy import select

from otvetoved_core.domain.models import UserSession, User
from otvetoved_core.infrastructure.database import DatabaseSession
from otvetoved_core.infrastructure.dto import BaseDTO, BaseRootDTO

from otvetoved_core.domain.models.question import Question

router = APIRouter(prefix="/questions")

QuestionBrief = Annotated[str, Field(
    title=
    "Question brief.",
    description=
    "Summary of the question to be displayed as question header.",
)]

QuestionText = Annotated[str, Field(
    title=
    "Question text.",
    description=
    "Text of the question.  Can be omitted, if question brief "
    "contains enough information about the question."
)]

QuestionId = Annotated[int, Field(
    title=
    "Question id.",
    description=
    "Question identifier.",
)]

QuestionUserID = Annotated[int, Field(
    title=
    "User id.",
    description=
    "Id of user which created this question.",
)]

TagID = Annotated[int, Field(
    title=
    "Tag id",
    description=
    "Tag id.",
)]

TagName = Annotated[str, Field(
    title=
    "Tag name.",
    description=
    "Name of this tag.",
)]

TagDescription = Annotated[str, Field(
    title=
    "Tag description.",
    description=
    "Description of this tag.",
)]

SessionToken = Annotated[UUID4, Field(
    title=
    "Session token.",
    description=
    "Generated token only for this session, which you use for another requests.",
)]


class QuestionTag(BaseDTO):
    id: TagID
    name: TagName
    description: TagDescription


class QuestionDTO(BaseDTO):
    """ A question """

    id: QuestionId
    brief: QuestionBrief
    text: QuestionText


class CreateQuestionDTO(BaseDTO):
    """ Create question request """

    brief: QuestionBrief
    text: QuestionText
    session_token: SessionToken


class QuestionFullInfoDTO(BaseDTO):
    """ A question with full info"""
    id: QuestionId
    brief: QuestionBrief
    text: QuestionText
    created_by_user_id: QuestionUserID
    tags: list[QuestionTag]


@router.post(
    "",
    response_model=QuestionDTO,
)
@inject
async def create_question(
        payload: CreateQuestionDTO,
        session: FromDishka[DatabaseSession],
):
    stmt = select(UserSession).where(UserSession.session_token == payload.session_token)
    user_sessions = await session.scalars(stmt)
    user_session: UserSession = user_sessions.one_or_none()
    if not user_session:
        raise HTTPException(404, f"Session with token {payload.session_token} not found")

    question = Question(
        brief=payload.brief,
        text=payload.text,
        created_by_user_id=user_session.user_id,
    )
    session.add(question)
    await session.flush()
    await session.commit()

    return QuestionDTO.model_validate(question)


QuestionListDTO = BaseRootDTO[list[QuestionDTO]]


@router.get(
    "",
    response_model=QuestionListDTO,
)
@inject
async def get_questions_list(
        session: FromDishka[DatabaseSession],
):
    stmt = select(Question)
    questions = await session.scalars(stmt)
    return QuestionListDTO.model_validate(questions)


@router.get(
    "{question_id}",
    response_model=QuestionFullInfoDTO,
)
@inject
async def get_question(
        session: FromDishka[DatabaseSession],
        question_id: int,
):
    stmt = select(Question).where(Question.id == question_id)
    questions = await session.scalars(stmt)
    question = questions.one_or_none()
    if not question:
        raise HTTPException(404, "Question with this is not found")
    return QuestionFullInfoDTO.model_validate(question)

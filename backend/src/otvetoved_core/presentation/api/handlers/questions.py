from datetime import datetime

from dishka.integrations.fastapi import inject, FromDishka
from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from otvetoved_core.domain.models import UserSession
from otvetoved_core.domain.models.question import Question
from otvetoved_core.infrastructure.database import DatabaseSession
from otvetoved_core.infrastructure.dto import BaseRootDTO
from otvetoved_core.presentation.api.schemas.schemas import (
    QuestionDTO,
    CreateQuestionDTO,
    QuestionFullInfoDTO,
)

router = APIRouter(prefix="/questions", tags=["questions"])


@router.post(
    "",
    response_model=QuestionDTO,
    name="Создать новый вопрос",
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
        create_time=int(datetime.now().timestamp()),
    )
    session.add(question)
    await session.flush()
    await session.commit()

    return QuestionDTO.model_validate(question)


QuestionListDTO = BaseRootDTO[list[QuestionDTO]]


@router.get(
    "",
    response_model=QuestionListDTO,
    name="Получить список вопросов",
)
@inject
async def get_questions_list(
        session: FromDishka[DatabaseSession],
):
    stmt = select(Question)
    questions = await session.scalars(stmt)
    return QuestionListDTO.model_validate(questions)


@router.get(
    "/{question_id}",
    response_model=QuestionFullInfoDTO,
    name="Получить конкретный вопрос по id"
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

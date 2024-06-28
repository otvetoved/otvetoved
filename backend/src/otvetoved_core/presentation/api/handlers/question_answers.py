from dishka.integrations.fastapi import inject, FromDishka
from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from otvetoved_core.domain.models.question import QuestionAnswer
from otvetoved_core.domain.models.user_session import UserSession
from otvetoved_core.infrastructure.database import DatabaseSession
from otvetoved_core.infrastructure.dto import BaseRootDTO
from otvetoved_core.presentation.api.schemas.schemas import CreateQuestionAnswerDTO, QuestionAnswerResponse

router = APIRouter(prefix="/questions/{question_id}/answers", tags=["answers"])


@router.post(
    "",
    response_model=QuestionAnswerResponse,
)
@inject
async def leave_answer(
        question_id: int,
        payload: CreateQuestionAnswerDTO,
        session: FromDishka[DatabaseSession],
):
    """"""

    stmt = select(UserSession).where(UserSession.session_token == payload.session_token)
    user_sessions = await session.scalars(stmt)
    user_session: UserSession = user_sessions.one_or_none()
    if not user_session:
        raise HTTPException(404, f"Session with token {payload.session_token} not found")
    answer = QuestionAnswer(
        question_id=question_id,
        created_by_user_id=user_session.user_id,
        text=payload.text,
    )
    session.add(answer)
    await session.flush()
    await session.commit()

    return QuestionAnswerResponse.model_validate(answer)


AnswerListDTO = BaseRootDTO[list[QuestionAnswerResponse]]


@router.get(
    "",
    response_model=AnswerListDTO,
)
@inject
async def get_answers(
        question_id: int,
        session: FromDishka[DatabaseSession],
):
    stmt = select(QuestionAnswer).where(QuestionAnswer.question_id == question_id)
    answers = await session.scalars(stmt)
    return AnswerListDTO.model_validate(answers)

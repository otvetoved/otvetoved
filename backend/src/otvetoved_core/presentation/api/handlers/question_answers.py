import bcrypt
from dishka.integrations.fastapi import inject, FromDishka
from fastapi import APIRouter, HTTPException
from sqlalchemy import select, ScalarResult

from otvetoved_core.infrastructure.database import DatabaseSession

from otvetoved_core.domain.models.user import User
from otvetoved_core.domain.models.user_session import UserSession
from otvetoved_core.presentation.api.schemas.schemas import QuestionAnswer, QuestionAnswerResponse

router = APIRouter(prefix="/questions/{question_id}/answers", tags=["answers"])


@router.post(
    "",
    response_model=QuestionAnswerResponse,
)
@inject
async def leave_answer(
    question_id: int,
    payload: QuestionAnswer
):
    pass


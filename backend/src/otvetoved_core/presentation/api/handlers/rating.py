from dishka.integrations.fastapi import inject, FromDishka
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import UUID4
from sqlalchemy import select

from otvetoved_core.domain.models import UserSession
from otvetoved_core.domain.models.question import UserAction, QuestionAnswer
from otvetoved_core.infrastructure.database import DatabaseSession
from otvetoved_core.presentation.api.schemas.schemas import (
    QuestionAnswerRatingDTO, AnswerRatingActionDTO, UserRateDTO,
)

router = APIRouter(prefix="/answers/{answer_id}/rating", tags=["rating"])


@router.put(
    "",
    status_code=200,
    name="Проголосовать за ответ на вопрос",
    response_model=QuestionAnswerRatingDTO,
    responses={
        404: {
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Session with token TOKEN not found",
                        "object": "session"
                    }
                }
            },
        }
    },
)
@inject
async def change_answer_rating(
        payload: AnswerRatingActionDTO,
        session: FromDishka[DatabaseSession],
        answer_id: int,
):
    """
    В случае если не найдена сессия\n
    "object": "session"\n
    если не найден ответ\n
    "object": "answer"
    """
    stmt = select(UserSession).where(UserSession.session_token == payload.session_token)
    user_sessions = await session.scalars(stmt)
    user_session: UserSession = user_sessions.one_or_none()
    if not user_session:
        return JSONResponse(
            status_code=404,
            content={
                "detail": f"Session with token {payload.session_token} not found",
                "object": "session",
            }
        )

    stmt = select(QuestionAnswer).where(QuestionAnswer.id == answer_id)
    answers = await session.scalars(stmt)
    answer = answers.one_or_none()
    if not answer:
        return JSONResponse(
            status_code=404,
            content={
                "detail": f"Answer with id {answer_id} not found",
                "object": "answer",
            }
        )

    stmt = select(UserAction).where(UserAction.user_id == user_session.user_id). \
        where(UserAction.answer_id == answer_id)
    rates = await session.scalars(stmt)
    rate = rates.one_or_none()

    if rate and rate.action == payload.action:
        # raise HTTPException(403, detail="User already voted")
        # Дальше идёт костыль, реализованный за пару часов до презентации продукта
        # TODO: исправить костыль
        await session.delete(rate)
        await session.flush()
        await session.commit()

        await session.refresh(answer)
        return QuestionAnswerRatingDTO.model_validate(answer)

    elif rate and rate.action != payload.action:
        await session.delete(rate)
        await session.flush()
        await session.commit()

    user_action = UserAction(
        answer_id=answer_id,
        user_id=user_session.user_id,
        action=payload.action
    )
    session.add(user_action)
    await session.flush()
    await session.commit()

    await session.refresh(answer)

    return QuestionAnswerRatingDTO.model_validate(answer)


@router.get(
    "",
    name="Получить голоса за ответ на вопрос",
    response_model=QuestionAnswerRatingDTO,
    responses={
        404: {
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Question not found",
                    }
                }
            },
        }
    },
)
@inject
async def get_answer_rating(
        session: FromDishka[DatabaseSession],

        answer_id: int,
):
    stmt = select(QuestionAnswer).where(QuestionAnswer.id == answer_id)
    answer = (await session.scalars(stmt)).one_or_none()
    if not answer:
        raise HTTPException(404, "Question not found")
    return QuestionAnswerRatingDTO.model_validate(answer)


@router.get(
    "/me",
    name="Получить свой ответ",
    status_code=200,
    response_model=UserRateDTO,
    responses={

    }
)
@inject
async def get_my_rate(
        session_token: UUID4,
        answer_id: int,
        session: FromDishka[DatabaseSession],
):
    stmt = select(UserSession).where(UserSession.session_token == session_token)
    user_session: UserSession = (await session.scalars(stmt)).one_or_none()
    if not user_session:
        return JSONResponse(
            status_code=404,
            content={
                "detail": f"Session {session_token} not found",
                "object": "session",
            }
        )
    stmt = select(UserAction).where(UserAction.answer_id == answer_id).where(UserAction.user_id == user_session.user_id)
    rate: QuestionAnswer = (await session.scalars(stmt)).one_or_none()
    if not rate:
        return JSONResponse(
            status_code=404,
            content={
                "detail": f"Answer {answer_id} not found",
                "object": "answer",
            }
        )
    return UserRateDTO.model_validate(rate)

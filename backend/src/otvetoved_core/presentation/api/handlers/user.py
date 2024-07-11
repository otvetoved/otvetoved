from dishka.integrations.fastapi import inject, FromDishka
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import select

from otvetoved_core.domain.models.user import User
from otvetoved_core.infrastructure.database import DatabaseSession
from otvetoved_core.presentation.api.schemas.schemas import UserTotalRateDTO

router = APIRouter(prefix="/user/{user_id}", tags=["user"])


@router.get(
    "/total_rate",
    name="",
    status_code=200,
    response_model=UserTotalRateDTO,
    responses={
        404: {
            "content": {
                "application/json": {
                    "example": {
                        "detail": "User with id {id} not found",
                        "object": "user"
                    }
                }
            },
        }
    },
)
@inject
async def get_total_rate(
        user_id: int,
        session: FromDishka[DatabaseSession]
):
    stmt = select(User).where(User.id == user_id)
    user: User = (await session.scalars(stmt)).one_or_none()
    if not user:
        return JSONResponse(
            content={
                "detail": f"User with id {user_id} not found",
                "object": "user"
            }
        )
    return UserTotalRateDTO.model_validate(user)

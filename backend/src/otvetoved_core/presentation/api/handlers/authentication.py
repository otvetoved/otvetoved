import bcrypt
from dishka.integrations.fastapi import inject, FromDishka
from fastapi import APIRouter, HTTPException
from sqlalchemy import select, ScalarResult

from otvetoved_core.domain.models.user import User
from otvetoved_core.domain.models.user_session import UserSession
from otvetoved_core.infrastructure.database import DatabaseSession
from ..schemas.schemas import AuthResponseDTO, AuthDTO, UserRegisterResponse, \
    UserRegisterForm

router = APIRouter(prefix="/authentication")


# TODO: сделать так, чтобы было всего 5 сессий на пользователя и у них было время жизни

@router.post(
    "",
    response_model=AuthResponseDTO,
    tags=["authentication"],
)
@inject
async def create_new_session(
        payload: AuthDTO,
        session: FromDishka[DatabaseSession],
):
    stmt = select(User) \
        .where(User.username == payload.username)
    users: ScalarResult = await session.scalars(stmt)
    user: User = users.one_or_none()
    if user is None or \
            not bcrypt.checkpw(password=payload.password.encode(),
                               hashed_password=user.password.encode("utf-8")):
        raise HTTPException(status_code=403, detail="Invalid password or username")

    user_session = UserSession(
        user_id=user.id
    )
    session.add(user_session)
    await session.flush()
    await session.commit()

    return AuthResponseDTO.model_validate(user_session)


@router.post(
    "/register",
    response_model=UserRegisterResponse,
    tags=["authentication"],
)
@inject
async def create_new_account(
        payload: UserRegisterForm,
        session: FromDishka[DatabaseSession],
):
    stmt = select(User).where(User.username == payload.username)
    users: ScalarResult = await session.scalars(stmt)
    if users.one_or_none():
        raise HTTPException(403, "User with this username already exists")
    salt = bcrypt.gensalt()
    user = User(
        first_name=payload.first_name,
        last_name=payload.last_name,
        username=payload.username,
        password=bcrypt.hashpw(salt=salt, password=payload.password.encode()).decode("utf-8")
    )
    session.add(user)
    await session.flush()
    await session.commit()

    return UserRegisterResponse.model_validate(user)

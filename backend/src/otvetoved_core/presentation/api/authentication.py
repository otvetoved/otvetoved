from typing import Annotated

from fastapi import APIRouter, HTTPException
from pydantic import Field, ConfigDict, UUID4
from dishka.integrations.fastapi import inject, FromDishka
from sqlalchemy import select, ScalarResult
import bcrypt

from otvetoved_core.infrastructure.database import DatabaseSession
from otvetoved_core.infrastructure.dto import BaseDTO

from otvetoved_core.domain.models.user import User
from otvetoved_core.domain.models.user_session import UserSession

router = APIRouter(prefix="/authentication")

'''
example for me
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


class QuestionDTO(BaseDTO):
    """ A question """

    id: QuestionId
    brief: QuestionBrief
    text: QuestionText


class CreateQuestionDTO(BaseDTO):
    """ Create question request """

    brief: QuestionBrief
    text: QuestionText


@router.post(
    "",
    response_model=QuestionDTO,
)
@inject
async def create_question(
        payload: CreateQuestionDTO,
        session: FromDishka[DatabaseSession],
):
    question = Question(
        brief=payload.brief,
        text=payload.text,
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
'''

SessionToken = Annotated[UUID4, Field(
    title=
    "Session token.",
    description=
    "Generated token only for this session, which you use for another requests.",
)]

Username = Annotated[str, Field(
    title=
    "User username.",
    description=
    "User username.",
)]

Password = Annotated[str, Field(
    title=
    "User password.",
    description=
    "User password.",
)]

UserID = Annotated[str, Field(
    title=
    "User id.",
    description=
    "Uniq user id.",
)]

FirstName = Annotated[str, Field(
    title=
    "First name",
    description=
    "User's first name.",
)]

LastName = Annotated[str, Field(
    title=
    "Last name.",
    description=
    "User's last name.",
)]


class AuthResponseDTO(BaseDTO):
    """An authentication response"""
    session_token: SessionToken


class AuthDTO(BaseDTO):
    """An authentication"""
    username: Username
    password: Password


class UserRegisterResponse(BaseDTO):
    """User info. Returns after registration"""
    username: Username
    id: UserID

    model_config = ConfigDict(coerce_numbers_to_str=True)


class UserRegisterForm(BaseDTO):
    """User info, which uses for registration"""
    username: Username
    password: Password
    first_name: FirstName
    last_name: LastName


# TODO: сделать так, чтобы было всего 5 сессий на пользователя и у них было время жизни

@router.post(
    "",
    response_model=AuthResponseDTO,
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

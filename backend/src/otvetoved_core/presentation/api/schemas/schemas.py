from typing import Annotated

from pydantic import Field, ConfigDict, UUID4
from otvetoved_core.infrastructure.dto import BaseDTO

Username = Annotated[str, Field(
    title=
    "Юзернейм пользователя.",
    description=
    "Имя в приложении, по которому можно идентифицировать пользователя. "
    "Может использоваться вместо id, если на то есть объективные причины.",
)]

Password = Annotated[str, Field(
    title=
    "Пароль.",
)]

UserID = Annotated[str, Field(
    title=
    "Идентификатор пользователя.",
)]

FirstName = Annotated[str, Field(
    title=
    "Имя.",
)]

LastName = Annotated[str, Field(
    title=
    "Фамилия.",
)]

QuestionBrief = Annotated[str, Field(
    title=
    "Краткое содержание вопроса.",
    description=
    "Краткое содержание вопроса, которое будет отображаться как "
    "заголовок этого вопроса.",
)]

QuestionText = Annotated[str | None, Field(
    title=
    "Текст вопроса",
    description=
    "Текст вопроса.  Может быть опущен, если краткое содержание вопроса"
    " содержит достаточно информации о вопросе."
)]

QuestionId = Annotated[int, Field(
    title=
    "Идентификатор вопроса.",
)]

QuestionUserID = Annotated[int, Field(
    title=
    "Идентификатор создателя вопроса.",
)]

TagID = Annotated[int, Field(
    title=
    "Идентификатор тега",
)]

TagName = Annotated[str, Field(
    title=
    "Название тега.",
)]

TagDescription = Annotated[str, Field(
    title=
    "Описание тега.",
)]

SessionToken = Annotated[UUID4, Field(
    title=
    "Токен сессии.",
    description=
    "Токен, сгенерированный для сессии входа.  Передается в другие"
    " запросы для подтверждения того, что их выполняет владелец этой"
    " сессии.",
)]


class QuestionTag(BaseDTO):
    id: TagID
    name: TagName
    description: TagDescription


class QuestionDTO(BaseDTO):
    """ Вопрос """

    id: QuestionId
    brief: QuestionBrief
    text: QuestionText


class CreateQuestionDTO(BaseDTO):
    """ Запрос на создание пользователя """

    brief: QuestionBrief
    text: QuestionText
    session_token: SessionToken


class QuestionFullInfoDTO(BaseDTO):
    """ Полная информация о вопросе """

    id: QuestionId
    brief: QuestionBrief
    text: QuestionText
    created_by_user_id: QuestionUserID
    tags: list[QuestionTag]


class AuthResponseDTO(BaseDTO):
    """ Ответ на запрос аутентификации """

    session_token: SessionToken


class AuthDTO(BaseDTO):
    """ Запрос аутентификации """

    username: Username
    password: Password


class UserRegisterResponse(BaseDTO):
    """ Информация о текущем пользователе """

    username: Username
    id: UserID

    model_config = ConfigDict(coerce_numbers_to_str=True)


class UserRegisterForm(BaseDTO):
    """ Полезная нагрузка запроса регистрации """

    username: Username
    password: Password
    first_name: FirstName
    last_name: LastName

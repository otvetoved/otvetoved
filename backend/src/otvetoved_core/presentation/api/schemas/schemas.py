from typing import Annotated

from pydantic import Field, ConfigDict, UUID4
from otvetoved_core.infrastructure.dto import BaseDTO

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

from typing import Annotated

from fastapi import APIRouter
from pydantic import Field
from dishka.integrations.fastapi import inject, FromDishka
from sqlalchemy import select

from otvetoved_core.infrastructure.database import DatabaseSession
from otvetoved_core.infrastructure.dto import BaseDTO, BaseRootDTO

from otvetoved_core.domain.models import Question


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

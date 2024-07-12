from sqladmin import ModelView

from otvetoved_core.domain.models import Question


class QuestionView(ModelView, model=Question):
    column_list = [
        Question.id,
        Question.brief,
        Question.text,
        Question.created_by_user,
        Question.created_at,
    ]

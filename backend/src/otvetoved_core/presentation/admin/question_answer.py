from sqladmin import ModelView

from otvetoved_core.domain.models import QuestionAnswer


class QuestionAnswerView(ModelView, model=QuestionAnswer):
    column_list = [
        QuestionAnswer.id,
        QuestionAnswer.question,
        QuestionAnswer.text,
        QuestionAnswer.created_by_user,
    ]

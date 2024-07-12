from sqladmin import ModelView

from otvetoved_core.domain.models import User


class UserView(ModelView, model=User):
    column_list = [
        User.id,
        User.username,
        User.email,
        User.sessions,
    ]

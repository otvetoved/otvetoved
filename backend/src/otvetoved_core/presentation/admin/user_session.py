from sqladmin import ModelView

from otvetoved_core.domain.models import UserSession


class UserSessionView(ModelView, model=UserSession):
    column_list = [
        UserSession.id,
        UserSession.user,
        UserSession.session_token,
        UserSession.created_at,
    ]

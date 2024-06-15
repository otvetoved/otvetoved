from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped

from app.src.otvetoved_core.infrastructure.entity import BaseEntity
from app.src.otvetoved_core.infrastructure.database import RelationalMapper


class BaseRelationalObject(BaseEntity, RelationalMapper):
    __abstract__ = True


class BaseRelationalEntity(BaseRelationalObject):
    __abstract__ = True

    if TYPE_CHECKING:  # I believe in the developers' neatness
        id: Mapped[int]


__all__ = [
    "BaseRelationalObject",
    "BaseRelationalEntity",
]

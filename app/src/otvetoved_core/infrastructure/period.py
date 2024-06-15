from functools import cached_property

from datetime import datetime

from app.src.otvetoved_core.infrastructure.dto import BaseDTO


class Period(BaseDTO):
    starts_at: datetime
    ends_at: datetime

    @cached_property
    def delta(self):
        return self.ends_at - self.starts_at

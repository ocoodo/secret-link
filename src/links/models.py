from sqlalchemy.orm import Mapped, mapped_column
#from sqlalchemy.sql import func

from datetime import datetime, timedelta
from typing import Optional

from src.database import Model


class Link(Model):
    __tablename__ = "links"
    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str] = mapped_column(nullable=True)
    content: Mapped[str]
    is_consumed: Mapped[bool] = mapped_column(default=False)

    @property
    def is_active(self) -> bool:
        return not self.is_consumed
        
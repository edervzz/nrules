""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .auditable import Auditable
from .base import Base


class Rule(Base, Auditable):
    """ Rule entity """

    __tablename__ = "rules"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", nullable=False)

    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    expression: Mapped[str] = mapped_column(nullable=False)

    is_exclusive: Mapped[bool] = mapped_column(nullable=True)

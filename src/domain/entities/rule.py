""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .base import Base
from .auditable import Auditable


class Rule(Base, Auditable):
    """ Rule entity """

    __tablename__ = "rules"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", nullable=False)

    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    operator: Mapped[str] = mapped_column(nullable=True)

    expression: Mapped[str] = mapped_column(nullable=False)

    order: Mapped[int] = mapped_column(nullable=True)

    is_multi_assignment: Mapped[bool] = mapped_column(nullable=True)

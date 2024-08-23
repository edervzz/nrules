""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .auditable import Auditable
from .base import Base


class Rule(Base, Auditable):
    """ Rule entity """

    __tablename__ = "rules"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False)

    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    expression: Mapped[str] = mapped_column(nullable=False)

    is_exclusive: Mapped[bool] = mapped_column(nullable=True)

    version: Mapped[int] = mapped_column(nullable=False)

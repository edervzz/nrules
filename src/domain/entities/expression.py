""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned
from .base import Base


class Expression(Base, Auditable, Versioned):
    """ Rule entity """

    __tablename__ = "expressions"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False)

    expression: Mapped[str] = mapped_column(nullable=False)

""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned, TenantSpecific
from .base import Base


class Expression(Base, TenantSpecific, Auditable, Versioned):
    """ entity """

    __tablename__ = "expressions"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    condition_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    expression: Mapped[str] = mapped_column(nullable=False)

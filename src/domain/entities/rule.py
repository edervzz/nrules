""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned, TenantSpecific
from .base import Base


class Rule(Base, TenantSpecific, Auditable, Versioned):
    """ Rule entity """

    __tablename__ = "rules"

    id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)

    is_zero_condition: Mapped[bool] = mapped_column(nullable=False)

    kvs_id: Mapped[int] = mapped_column(nullable=True)

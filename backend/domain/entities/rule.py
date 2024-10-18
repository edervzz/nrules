""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned, TenantSpecific
from .base import Base


class Rule(Base, TenantSpecific, Auditable, Versioned):
    """ Rule entity """

    __tablename__ = "rules"

    id: Mapped[str] = mapped_column(
        primary_key=True, nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)

    rule_type: Mapped[str] = mapped_column(nullable=False)

    strategy: Mapped[str] = mapped_column(nullable=True)

    kvs_id_nok: Mapped[int] = mapped_column(nullable=True)

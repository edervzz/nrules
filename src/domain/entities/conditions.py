""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned, TenantSpecific
from .base import Base


class Condition(Base, TenantSpecific, Auditable, Versioned):
    """ Rule entity """

    __tablename__ = "conditions"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    rule_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    expression: Mapped[str] = mapped_column(nullable=False)

    position: Mapped[int] = mapped_column(nullable=False)

    kvs_id: Mapped[int] = mapped_column(nullable=True)

    kvs_id_nok: Mapped[int] = mapped_column(nullable=True)

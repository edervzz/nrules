""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned, TenantSpecific
from .base import Base


class Rule(Base, TenantSpecific, Auditable, Versioned):
    """ Rule entity.

        Works like container of conditions and kv items
        Depending of type and strategy it run and get result from cases
    """

    __tablename__ = "rules"

    id: Mapped[str] = mapped_column(
        primary_key=True, nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)

    rule_type: Mapped[str] = mapped_column(nullable=False)

    strategy: Mapped[str] = mapped_column(nullable=True)

    default_kvs_id: Mapped[int] = mapped_column(nullable=True)

    is_active: Mapped[bool] = mapped_column(nullable=False)

    is_archived: Mapped[bool] = mapped_column(nullable=True)

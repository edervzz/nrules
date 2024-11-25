""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, TenantSpecific
from .base import Base


class Case(Base, TenantSpecific, Auditable):
    """ Case entity """

    __tablename__ = "cases"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    rule_id: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    position: Mapped[int] = mapped_column(nullable=False)

    condition_group_id: Mapped[str] = mapped_column(nullable=True)

    kv_storage_id: Mapped[int] = mapped_column(nullable=True)

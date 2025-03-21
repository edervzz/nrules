""" Entities """
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from .base import Base
from .extra_fields import Auditable, TenantSpecific


class Case(Base, TenantSpecific, Auditable):
    """ Case entity. 

        A Case integrate a set of conditions to be commit (condition group)
        when it's success return KV storage associated.
        Them depends of strategy of its rule and order (position)
    """

    __tablename__ = "cases"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    rule_id: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    position: Mapped[int] = mapped_column(nullable=False)

    is_active: Mapped[bool] = mapped_column(nullable=False)

    is_archived: Mapped[bool] = mapped_column(nullable=True)

""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, TenantSpecific
from .base import Base


class ConditionGroup(Base, TenantSpecific, Auditable):
    """ Condition group entity """

    __tablename__ = "condition_groups"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False)

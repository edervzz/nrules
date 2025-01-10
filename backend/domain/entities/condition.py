""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, TenantSpecific
from .base import Base


class Condition(Base, TenantSpecific, Auditable):
    """ Condition entity.  

    Define variables related with its operator and value (var eq value)
    They are associated with only one condition group.
    """

    __tablename__ = "conditions"

    variable: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    condition_group_id: Mapped[str] = mapped_column(
        primary_key=True, nullable=False)

    operator: Mapped[str] = mapped_column(nullable=False)

    value: Mapped[str] = mapped_column(nullable=False)

    typeof: Mapped[str] = mapped_column(nullable=False)

    is_active: Mapped[bool] = mapped_column(nullable=False)

    is_archived: Mapped[bool] = mapped_column(nullable=True)

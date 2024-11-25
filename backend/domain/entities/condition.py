""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, TenantSpecific
from .base import Base


class Condition(Base, TenantSpecific, Auditable):
    """ Condition entity """

    __tablename__ = "conditions"

    variable: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    condition_group_id: Mapped[str] = mapped_column(
        primary_key=True, nullable=False)

    operator: Mapped[str] = mapped_column(nullable=False)

    value: Mapped[str] = mapped_column(nullable=False)

    typeof: Mapped[str] = mapped_column(nullable=False)

    is_case_sensitive: Mapped[bool] = mapped_column(nullable=False)

    is_visible: Mapped[bool] = mapped_column(nullable=False)

    is_deleted: Mapped[bool] = mapped_column(nullable=False)

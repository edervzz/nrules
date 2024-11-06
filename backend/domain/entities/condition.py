""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, TenantSpecific
from .base import Base


class Condition(Base, TenantSpecific, Auditable):
    """ Condition entity """

    __tablename__ = "conditions"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    condition_id: Mapped[str] = mapped_column(nullable=False)

    variable: Mapped[str] = mapped_column(nullable=False)

    operator: Mapped[str] = mapped_column(nullable=False)

    value: Mapped[str] = mapped_column(nullable=False)

    is_case_sensitive: Mapped[bool] = mapped_column(nullable=True)

    typeof: Mapped[str] = mapped_column(nullable=False)

""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned, TenantSpecific
from .base import Base


class Parameters(Base, TenantSpecific, Auditable, Versioned):
    """ Rule entity """

    __tablename__ = "conditions"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    field: Mapped[str] = mapped_column(nullable=False)

    param_type: Mapped[str] = mapped_column(nullable=False)

    field: Mapped[str] = mapped_column(nullable=False)

    typeof: Mapped[str] = mapped_column(nullable=False)

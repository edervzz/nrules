""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned, TenantSpecific
from .base import Base


class Parameter(Base, TenantSpecific, Auditable, Versioned):
    """ A Parameter is a variable into expression or output """

    __tablename__ = "parameters"

    key: Mapped[str] = mapped_column(nullable=False)

    rule_id: Mapped[str] = mapped_column(nullable=False)

    usefor: Mapped[str] = mapped_column(nullable=False)

    typeof: Mapped[str] = mapped_column(nullable=False)

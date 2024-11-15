""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, TenantSpecific
from .base import Base


class Parameter(Base, TenantSpecific, Auditable):
    """ A Parameter is a variable into expression or output """

    __tablename__ = "parameters"

    key: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    rule_id: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    usefor: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    typeof: Mapped[str] = mapped_column(nullable=False)

    is_case_sensitive: Mapped[bool] = mapped_column(nullable=True)

    is_hidden: Mapped[bool] = mapped_column(nullable=True)

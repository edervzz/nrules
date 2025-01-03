""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, TenantSpecific
from .base import Base


class Tag(Base, TenantSpecific, Auditable):
    """ Tag entity """

    __tablename__ = "tags"

    rule_id: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    key: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    value: Mapped[str] = mapped_column(nullable=True)

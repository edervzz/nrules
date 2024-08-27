""" workflow rule """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned
from .base import Base


class Variant(Base, Auditable, Versioned):
    """ Container entity """

    __tablename__ = "variants"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    key: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    entrypoint_key: Mapped[int] = mapped_column(nullable=False)

    value: Mapped[str] = mapped_column(nullable=False)

    version: Mapped[int] = mapped_column(nullable=False)

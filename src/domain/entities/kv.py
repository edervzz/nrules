""" _summry_ """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned
from .base import Base


class KV(Base, Auditable, Versioned):
    """ Key-Value Item entity """

    __tablename__ = "kvs"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)

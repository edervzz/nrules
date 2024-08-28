""" _summry_ """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned
from .base import Base


class KVItem(Base, Auditable, Versioned):
    """ Key-Value Item entity """

    __tablename__ = "kv_items"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    key: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    kv_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    value: Mapped[str] = mapped_column(nullable=False)

    typeof: Mapped[str] = mapped_column(nullable=True)

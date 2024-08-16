""" _summry_ """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .auditable import Auditable
from .base import Base


class KVItem(Base, Auditable):
    """ Key-Value Item entity """

    __tablename__ = "kv_items"

    kvs_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    key: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    value: Mapped[str] = mapped_column(nullable=False)

    type_value: Mapped[str] = mapped_column(nullable=True)

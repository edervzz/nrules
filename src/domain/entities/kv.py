""" _summry_ """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .auditable import Auditable
from .base import Base


class KV(Base, Auditable):
    """ Key-Value Item entity """

    __tablename__ = "kvs"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)

""" _summry_ """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import TenantSpecific, Auditable
from .base import Base


class KVStorage(Base, TenantSpecific, Auditable):
    """ Key-Value Storage entity """

    __tablename__ = "kv_storage"

    id: Mapped[str] = mapped_column(
        primary_key=True, nullable=False)

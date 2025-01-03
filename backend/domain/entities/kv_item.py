""" _summary_ """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import TenantSpecific, Auditable
from .base import Base


class KVItem(Base, TenantSpecific, Auditable):
    """ Key-Value Item entity.

        Key Value pair as result
    """

    __tablename__ = "kv_items"

    key: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    kv_id: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    value: Mapped[str] = mapped_column(nullable=False)

    calculation: Mapped[str] = mapped_column(nullable=True)

    typeof: Mapped[str] = mapped_column(nullable=True)

    is_active: Mapped[bool] = mapped_column(nullable=False)

    is_archived: Mapped[bool] = mapped_column(nullable=True)

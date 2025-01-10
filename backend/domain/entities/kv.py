""" _summry_ """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import TenantSpecific, Auditable
from .base import Base


class KV(Base, TenantSpecific, Auditable):
    """ Key-Value entity. 

        Group many KV Items.
    """

    __tablename__ = "kvs"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    rule_id: Mapped[str] = mapped_column(nullable=False)

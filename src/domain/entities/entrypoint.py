""" workflow rule """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned, TenantSpecific
from .base import Base


class Entrypoint(Base, TenantSpecific, Auditable, Versioned):
    """ Container entity """

    __tablename__ = "entrypoints"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)

    objty: Mapped[str] = mapped_column(nullable=False)

    objid: Mapped[int] = mapped_column(nullable=False)

    kvs_id_in: Mapped[int] = mapped_column(nullable=False)

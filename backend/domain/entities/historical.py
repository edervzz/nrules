""" Actions """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned
from .base import Base


class Historical(Base, Auditable, Versioned):
    """ historical """

    __tablename__ = "historical"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    objtype: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    objid: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    objver: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    data: Mapped[bytes] = mapped_column(nullable=False)

""" Actions """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned
from .base import Base


class Task(Base, Auditable, Versioned):
    """ Taks """

    __tablename__ = "tasks"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    order_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    objtype: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    objid: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    objver: Mapped[int] = mapped_column(nullable=False)

    action: Mapped[str] = mapped_column(nullable=False)

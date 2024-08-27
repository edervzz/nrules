""" workflow rule """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .auditable import Auditable
from .base import Base


class Container(Base, Auditable):
    """ Container entity """

    __tablename__ = "containers"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    workflow_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    rule_id: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    operator: Mapped[str] = mapped_column(nullable=False)

    order: Mapped[int] = mapped_column(nullable=False)

    action_id_ok: Mapped[int] = mapped_column(nullable=True)

    version: Mapped[int] = mapped_column(nullable=False)

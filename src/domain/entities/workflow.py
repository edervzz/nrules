""" workflow entity """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .auditable import Auditable
from .base import Base


class Workflow(Base, Auditable):
    """ Workflow entity """

    __tablename__ = "workflows"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)

    container_id: Mapped[int] = mapped_column(nullable=False)

    ok_workflow_id: Mapped[int] = mapped_column(nullable=False)

    ok_kvs_id: Mapped[int] = mapped_column(nullable=False)

    nok_workflow_id: Mapped[int] = mapped_column(nullable=False)

    nok_kvs_id: Mapped[int] = mapped_column(nullable=False)

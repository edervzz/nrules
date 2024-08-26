""" workflow rule """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .auditable import Auditable
from .base import Base


class Container(Base, Auditable):
    """ Container entity """

    __tablename__ = "container"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    is_node: Mapped[bool] = mapped_column(nullable=True)

    is_full: Mapped[bool] = mapped_column(nullable=True)


class ContainerRules(Base, Auditable):
    """ Container entity """

    __tablename__ = "container"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    container_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    rule_id: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    operator: Mapped[str] = mapped_column(nullable=False)

    order: Mapped[int] = mapped_column(nullable=True)

    ok_workflow_id: Mapped[int] = mapped_column(nullable=False)

    ok_kvs_id: Mapped[int] = mapped_column(nullable=False)

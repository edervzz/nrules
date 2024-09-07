""" workflow entity """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned
from .base import Base


class Node(Base, Auditable, Versioned):
    """ Node entity """

    __tablename__ = "nodes"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)

    typeof: Mapped[str] = mapped_column(nullable=True)

    action_id_ok: Mapped[int] = mapped_column(nullable=False)

    action_id_nok: Mapped[int] = mapped_column(nullable=False)

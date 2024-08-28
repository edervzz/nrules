""" workflow rule """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned
from .base import Base


class Entrypoint(Base, Auditable, Versioned):
    """ Container entity """

    __tablename__ = "entrypoints"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)

    workflow_id: Mapped[int] = mapped_column(nullable=False)

    is_active: Mapped[bool] = mapped_column(nullable=False)

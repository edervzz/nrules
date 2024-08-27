""" Actions """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned
from .base import Base


class Action(Base, Auditable, Versioned):
    """ Actions """

    __tablename__ = "actions"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)

    workflow_id: Mapped[int] = mapped_column(nullable=False)

    kv_id: Mapped[int] = mapped_column(nullable=False)

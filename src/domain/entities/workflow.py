""" workflow entity """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .auditable import Auditable
from .base import Base


class Workflow(Base, Auditable):
    """ Workflow entity """

    __tablename__ = "workflows"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)

    variant_id: Mapped[str] = mapped_column(nullable=True)

    is_node: Mapped[bool] = mapped_column(nullable=True)

    action_on_success: Mapped[int] = mapped_column(nullable=True)

    action_on_failure: Mapped[int] = mapped_column(nullable=True)

""" workflow entity """

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from toolkit import Base


class Workflow(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """
    __tablename__ = "workflows"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    variant_id: Mapped[str] = mapped_column(nullable=True)
    is_node: Mapped[bool] = mapped_column(nullable=True)
    success_action_id: Mapped[int] = mapped_column(nullable=True)
    failure_action_id: Mapped[int] = mapped_column(nullable=True)

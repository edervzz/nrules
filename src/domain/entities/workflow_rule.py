""" workflow rule """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .auditable import Auditable
from .base import Base


class WorkflowRule(Base, Auditable):
    """ Workflow-Rule entity """

    __tablename__ = "workflow_rules"

    workflow_id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False)

    rule_id: Mapped[str] = mapped_column(
        primary_key=True, nullable=False)

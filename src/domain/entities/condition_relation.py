""" asdf """
from sqlalchemy.orm import Mapped, mapped_column
from domain.entities.base import Base
from domain.entities.extra_fields import Auditable, Versioned


class ConditionRelation(Base, Auditable, Versioned):
    """ entity """

    __tablename__ = "condition_relations"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    condition_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    related_condition_id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False)

    relation_type: Mapped[str] = mapped_column(
        nullable=False)

    position: Mapped[int] = mapped_column(
        nullable=False)

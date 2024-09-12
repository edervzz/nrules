""" asdf """
from sqlalchemy.orm import Mapped, mapped_column
from domain.entities.base import Base
from domain.entities.extra_fields import Auditable, Versioned


class RuleRelation(Base, Auditable, Versioned):
    """ Nodes entity """

    __tablename__ = "rule_relations"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    rule_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    related_rule_id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False)

    relation_type: Mapped[str] = mapped_column(
        nullable=False)

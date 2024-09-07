""" Entities """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned
from .base import Base


class Rule(Base, Auditable, Versioned):
    """ Rule entity """

    __tablename__ = "rules"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)

    is_switch: Mapped[bool] = mapped_column(nullable=False)

    rule_id: Mapped[int] = mapped_column(nullable=True)

    kvs_id: Mapped[int] = mapped_column(nullable=True)


class Switches(Base, Auditable, Versioned):
    """ Switches entity """

    __tablename__ = "switches"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    rule_id1: Mapped[str] = mapped_column(nullable=False)

    rule_id2: Mapped[str] = mapped_column(nullable=False)

    rule_id3: Mapped[str] = mapped_column(nullable=False)

    rule_id4: Mapped[str] = mapped_column(nullable=False)

    rule_id5: Mapped[str] = mapped_column(nullable=False)

    rule_id6: Mapped[str] = mapped_column(nullable=False)

    rule_id7: Mapped[str] = mapped_column(nullable=False)

    rule_id8: Mapped[str] = mapped_column(nullable=False)

    rule_id9: Mapped[str] = mapped_column(nullable=False)

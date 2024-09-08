from domain.entities.base import Base
from domain.entities.extra_fields import Auditable, Versioned


from sqlalchemy.orm import Mapped, mapped_column


class Node(Base, Auditable, Versioned):
    """ Nodes entity """

    __tablename__ = "nodes"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    rule_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    mode: Mapped[str] = mapped_column(nullable=False)

    rule_id1: Mapped[str] = mapped_column(nullable=False)

    rule_id2: Mapped[str] = mapped_column(nullable=False)

    rule_id3: Mapped[str] = mapped_column(nullable=False)

    rule_id4: Mapped[str] = mapped_column(nullable=False)

    rule_id5: Mapped[str] = mapped_column(nullable=False)

    rule_id6: Mapped[str] = mapped_column(nullable=False)

    rule_id7: Mapped[str] = mapped_column(nullable=False)

    rule_id8: Mapped[str] = mapped_column(nullable=False)

    rule_id9: Mapped[str] = mapped_column(nullable=False)

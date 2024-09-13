"""_summary_
    """
from sqlalchemy.orm import Mapped, mapped_column
from domain.entities.base import Base
from domain.entities.extra_fields import Auditable


class XRule(Base, Auditable):
    """ X-Rules """

    __tablename__ = "xrules"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", nullable=False)

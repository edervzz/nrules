"""_summary_
    """
from domain.entities.base import Base
from domain.entities.extra_fields import Auditable
from sqlalchemy.orm import Mapped, mapped_column


class XObject(Base, Auditable):
    """ X-Object """

    __tablename__ = "xobject"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", nullable=False)

    object_name: Mapped[str] = mapped_column(nullable=False)

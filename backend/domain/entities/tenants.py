"""_summary_
    """
from sqlalchemy.orm import Mapped, mapped_column
from domain.entities.base import Base
from domain.entities.extra_fields import Auditable


class Tenants(Base, Auditable):
    """ Tenants """

    __tablename__ = "tenants"

    id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)

    stage: Mapped[str] = mapped_column(nullable=False)

    option: Mapped[str] = mapped_column(nullable=False)

    is_active: Mapped[bool] = mapped_column(nullable=True)

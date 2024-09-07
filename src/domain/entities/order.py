""" Actions """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .extra_fields import Auditable, Versioned
from .base import Base


class Order(Base, Auditable, Versioned):
    """ Order """

    __tablename__ = "orders"

    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    description: Mapped[str] = mapped_column(nullable=True)

    status: Mapped[str] = mapped_column(nullable=False)

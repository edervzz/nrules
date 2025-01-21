""" Entities """
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from .base import Base
from .extra_fields import TenantSpecific


class Lock(Base, TenantSpecific):
    """ Lock entity. 

        Used for keep rule edition assigned to only one user at time
    """

    __tablename__ = "cases"

    tablename: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    argument: Mapped[str] = mapped_column(primary_key=True, nullable=False)

    username: Mapped[str] = mapped_column(nullable=False)

    created_at: Mapped[int] = mapped_column(nullable=False)

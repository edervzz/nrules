""" Actions """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class XObject:
    """ X-Objects """

    __tablename__ = "xobjects"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", nullable=False)

    object_name: Mapped[str] = mapped_column(nullable=False)

""" auditable """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Auditable:
    """ Auditable field """
    created_by: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[str] = mapped_column(nullable=False)
    updated_by: Mapped[str] = mapped_column(nullable=False)
    updated_at: Mapped[str] = mapped_column(nullable=False)

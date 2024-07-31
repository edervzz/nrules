from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Rule:
    """ Rule entity """
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement="auto", nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    operator: Mapped[str] = mapped_column(nullable=True)
    expression: Mapped[str] = mapped_column(nullable=False)

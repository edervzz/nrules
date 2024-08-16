from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Migrations(Base):
    """ Migrations entity """

    __tablename__ = "__migrations"

    id: Mapped[str] = mapped_column(
        primary_key=True)

    exec_date: Mapped[str] = mapped_column(nullable=True)

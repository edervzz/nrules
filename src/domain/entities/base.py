""" entities basis """
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from .extra_fields import Auditable


class Base(DeclarativeBase):
    """ Base Class """


class Migrations(Base):
    """ Migrations entity """

    __tablename__ = "__migrations"

    id: Mapped[str] = mapped_column(
        primary_key=True)

    exec_date: Mapped[str] = mapped_column(nullable=True)


class XObject(Base, Auditable):
    """ X-Object """

    __tablename__ = "xobject"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", nullable=False)

    object_name: Mapped[str] = mapped_column(nullable=False)


class Tenants(Base, Auditable):
    """ Tenants """

    __tablename__ = "tenants"

    id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)


class TenantStages(Base, Auditable):
    """ Tenants Stages """

    __tablename__ = "tenant_stages"

    tenant_dev_id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False)

    tenant_test_id: Mapped[int] = mapped_column(nullable=False)

    tenant_release_id: Mapped[int] = mapped_column(nullable=False)

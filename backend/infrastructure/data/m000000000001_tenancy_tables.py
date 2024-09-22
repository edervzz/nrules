""" migration file """

from datetime import datetime
from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy import MetaData, Table, Engine, select, Boolean, BigInteger, BINARY
from sqlalchemy.orm import Session
from domain.entities import Migrations
from .audit import set_auditable


def tenancy_tables(engine: Engine) -> str:
    """000000000001_tenancy_tables"""

    name = "000000000001_tenancy_tables"

    stms = select(Migrations).where(Migrations.id == name)
    with Session(engine) as session:
        result = session.scalar(stms)
        if result is not None:
            return result.id

    metadata_obj = MetaData()

    # Historical Storage ----------------------------------------------
    history = Table(
        "historical",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "objtype", String(50), primary_key=True, comment="Object Type"),
        Column(
            "objid", BigInteger, primary_key=True, comment="Object ID"),
        Column(
            "objver", Integer, primary_key=True, comment="Version of Object", nullable=False),
        Column(
            "data", BINARY, comment="Data", nullable=False),
        comment="Variant is a container for many Key-Values"
    )
    set_auditable(history)

    # Tenant Storage ----------------------------------------------
    tenants = Table(
        "tenants",
        metadata_obj,
        Column(
            "id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "name", String(60), nullable=False, comment="Tenant Name", unique=True),
        Column(
            "stage", String(4), CheckConstraint("stage = 'DEV' OR stage = 'TEST' OR stage = 'PROD'", name="tenant_stages_chk_stage"), comment="Stage"),
        Column(
            "option", String(500), comment="Option"),
        Column(
            "is_active", Boolean, primary_key=True, comment="Tenant Is Active"),
        comment="Tenant Storage"
    )
    set_auditable(tenants)

    # Order Storage ----------------------------------------------
    order = Table(
        "orders",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", BigInteger, primary_key=True, autoincrement=True, comment="Order ID"),
        Column(
            "description", String(50), comment="Description of change"),
        Column(
            "status", String(1), CheckConstraint("status = 'D' OR status = 'R'", name="orders_chk_status"), comment="Order Status"),
        comment="Change Order"
    )
    set_auditable(order)

    # Taks Storage ----------------------------------------------
    task = Table(
        "tasks",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", BigInteger, primary_key=True, autoincrement=True, comment="Task ID"),
        Column(
            "order_id", BigInteger, primary_key=True, comment="Order ID"),
        Column(
            "objtype", String(50), primary_key=True, comment="Object Type"),
        Column(
            "objid", BigInteger, primary_key=True,  comment="Object ID"),
        Column(
            "objver", Integer, comment="Version of Object", nullable=False),
        Column(
            "action", String(4), CheckConstraint("action = 'NEW' OR action = 'EDIT' OR action = 'DEL'", name="tasks_chk_action"), comment="Action on Object", nullable=False),
        comment="Order of change"
    )
    set_auditable(task)

    metadata_obj.create_all(engine)

    with Session(engine) as session:
        m = Migrations()
        m.id = name
        m.exec_date = datetime.now()
        session.add(m)
        session.commit()
        return name

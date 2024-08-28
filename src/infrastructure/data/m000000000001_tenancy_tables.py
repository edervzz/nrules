""" migration file """

from datetime import datetime
from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy import MetaData, Table, Engine, select, Boolean
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

    # # Tenant Stage Storage ----------------------------------------------
    # tenants_stage = Table(
    #     "tenant_stages",
    #     metadata_obj,
    #     Column(
    #         "tenant_id", Integer, primary_key=True, comment="Tenant Development ID"),
    #     Column(
    #         "stage", String(4), CheckConstraint("stage = 'DEV' OR stage = 'TEST' OR stage = 'PROD'", name="tenant_stages_chk_stage"), comment="Stage"),

    #     comment="Tenant Stage Storage"
    # )
    # set_auditable(tenants_stage)

    metadata_obj.create_all(engine)

    with Session(engine) as session:
        m = Migrations()
        m.id = name
        m.exec_date = datetime.now()
        session.add(m)
        session.commit()
        return name

""" migration file """

from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy import MetaData, Table, CheckConstraint, Engine, select
from sqlalchemy.orm import Session
from domain.entities import Migrations
from .audit import set_auditable


def core_admin(engine: Engine) -> str:
    """000000000001_core_admin"""

    name = "000000000001_core_admin"

    metadata_obj = MetaData()

    stms = select(Migrations).where(Migrations.id == name)
    with Session(engine) as session:
        result = session.scalar(stms)
        if result is not None:
            return result.id

    # Idempotency Storage ----------------------------------------------
    idempotency = Table(
        "idempotency",
        metadata_obj,
        Column(
            "id", String(80),
            primary_key=True,
            autoincrement=True,
            comment="ID for idempotency"),
        Column(
            "status", String(3),
            CheckConstraint(
                "status = 'NEW' OR status = 'WIP' OR status = 'OK' OR status = 'NOK'", name="idempotency_chk_status"),
            nullable=True,
            comment="Status"),
        Column(
            "http_code", String(3),
            nullable=False,
            comment=""),
        Column(
            "headers", String(),
            nullable=False,
            comment=""),
        Column(
            "response", String(),
            nullable=False,
            comment=""),
        Column(
            "start_at", DateTime,
            comment="Start At", nullable=True),
        Column(
            "end_at", DateTime,
            comment="End At", nullable=True),
        comment="Idempotency"
    )
    set_auditable(idempotency)

    metadata_obj.create_all(engine)

    with Session(engine) as session:
        m = Migrations()
        m.id = name
        m.exec_date = datetime.now()
        session.add(m)
        session.commit()
        return name

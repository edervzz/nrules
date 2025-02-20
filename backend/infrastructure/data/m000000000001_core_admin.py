""" migration file """

from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy import MetaData, Table, CheckConstraint, Engine, select, UniqueConstraint
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

    # Locks ----------------------------------------------
    Table(
        "locks",
        metadata_obj,
        Column(
            "tablename", String(20),
            primary_key=True,
            comment="Table name"),
        Column(
            "argument", String(50),
            primary_key=True,
            comment="Argument"),
        Column(
            "username", String(50),
            nullable=False,
            comment="User name"),
        Column(
            "created_at", String(50),
            nullable=False,
            comment="Locked at time"),
    )

    # Idempotency Storage ----------------------------------------------
    idempotency = Table(
        "idempotency",
        metadata_obj,
        Column(
            "id", String(80),
            primary_key=True,
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
            "headers", String(80),
            nullable=False,
            comment=""),
        Column(
            "response", String(80),
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

  # Inventory ----------------------------------------------
    # inventory = Table(
    #     "inventory",
    #     metadata_obj,
    #     Column(
    #         "id", String(36),
    #         primary_key=True,
    #         comment="Inventory ID"),
    #     Column(
    #         "rule_id", String(36),
    #         nullable=False,
    #         comment="Rule ID"),
    #     Column(
    #         "version", String(10),
    #         nullable=False,
    #         comment="Version"),
    #     Column(
    #         "data_raw", String,
    #         comment="Rule Data"),
    #     Column(
    #         "is_active", Boolean,
    #         nullable=True,
    #         comment="Is Active Version"),
    #     Column(
    #         "is_cancelled", Boolean,
    #         nullable=False,
    #         comment="Is Canceled Version"),
    #     UniqueConstraint("rule_id", "version", name="inventory_unk"),
    # )
    # set_auditable(inventory)

    # Changes ----------------------------------------------
    # changes = Table(
    #     "changes",
    #     metadata_obj,
    #     Column(
    #         "id", String(36),
    #         primary_key=True,
    #         comment="Inventory ID"),
    #     Column(
    #         "rule_id", String(36),
    #         nullable=False,
    #         comment="Rule ID"),
    #     Column(
    #         "status", String(4),
    #         CheckConstraint(
    #             "status = 'OPEN' OR status = 'DONE' OR status = 'CANC'", name="changes_chk_status"),
    #         nullable=False,
    #         comment="Status of Change"),
    #     Column(
    #         "action", String(4),
    #         CheckConstraint(
    #             "action = 'CREA' OR action = 'UPDT' OR action = 'LOAD'", name="changes_chk_action"),
    #         nullable=False,
    #         comment="Status of Change"),
    #     Column(
    #         "ver_origin", String(10),
    #         nullable=False,
    #         comment="Origin Version"),
    #     Column(
    #         "ver_final", String(10),
    #         nullable=False,
    #         comment="Final Version"),
    #     Column(
    #         "is_recovery", Boolean,
    #         nullable=False,
    #         comment="Is recovered version")
    # )
    # set_auditable(changes)

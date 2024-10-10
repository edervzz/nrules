""" migration file """

from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, Boolean, Index
from sqlalchemy import MetaData, Table,  CheckConstraint, UniqueConstraint, Engine, select
from sqlalchemy.orm import Session
from domain.entities import Migrations
from .audit import set_auditable, set_version


def core_tables(engine: Engine) -> str:
    """000000000001_core_tables"""

    name = "000000000001_core_tables"

    metadata_obj = MetaData()

    stms = select(Migrations).where(Migrations.id == name)
    with Session(engine) as session:
        result = session.scalar(stms)
        if result is not None:
            return result.id

    # rule Relation ----------------------------------------------
    rule_relation = Table(
        "rule_relations",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "rule_id", BigInteger, primary_key=True, comment="Rule ID"),
        Column(
            "related_rule_id", BigInteger, primary_key=True, comment="Related Rule ID"),
        Column(
            "relation_type",
            String(3),
            CheckConstraint("relation_type = 'OK' OR relation_type = 'NOK'",
                            name="rule_relations_chk_relation_type"),
            nullable=False, comment="Relation type between rules"),
        comment="Relation between rules"
    )
    set_version(rule_relation)
    set_auditable(rule_relation)
    Index(
        "ix_rule_relations_001",
        rule_relation.c.tenant_id,
        rule_relation.c.related_rule_id)

    # Condition Relation ----------------------------------------------
    cond_relation = Table(
        "condition_relations",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "condition_id", BigInteger, primary_key=True, comment="Condition ID"),
        Column(
            "related_condition_id", BigInteger, primary_key=True, comment="Related Condition ID"),
        Column(
            "relation_type",
            String(3),
            CheckConstraint("relation_type = 'OK' OR relation_type = 'NOK'",
                            name="condition_relations_chk_relation_type"),
            nullable=False, comment="Relation type between conditions"),
        Column(
            "position", Integer, nullable=False, comment="Position between condition when they are assigned to same one"),
        comment="Relation between Conditions"
    )
    set_version(cond_relation)
    set_auditable(cond_relation)
    Index(
        "ix_condition_relations_001",
        cond_relation.c.tenant_id,
        cond_relation.c.related_condition_id)

    # Entrypoint Storage ----------------------------------------------
    entrypoint = Table(
        "entrypoints",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", Integer, primary_key=True, comment="Entrypoint ID"),
        Column(
            "name", String(50), nullable=False, unique=True, comment="Entrypoint's Name"),
        Column(
            "rule_id", BigInteger, comment="Rule ID"),
        Column(
            "kvs_id", Boolean, comment="KVS ID used as input"),
        comment="Entrypoint determine which Rules will be called"
    )
    set_version(entrypoint)
    set_auditable(entrypoint)
    Index(
        "ix_entrypoints_001",
        entrypoint.c.tenant_id,
        entrypoint.c.name)

    metadata_obj.create_all(engine)

    with Session(engine) as session:
        m = Migrations()
        m.id = name
        m.exec_date = datetime.now()
        session.add(m)
        session.commit()
        return name

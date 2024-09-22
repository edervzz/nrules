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

    # Key-Value Storage ----------------------------------------------
    kv = Table(
        "kvs",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", BigInteger, primary_key=True, comment="Key-Value Storage ID"),
        Column(
            "name", String(50), nullable=False, comment="Key-Value Storage Name", unique=True),
        comment="KVS is a container for many Key-Values"
    )
    set_version(kv)
    set_auditable(kv)
    Index(
        "ix_kvs_001",
        kv.c.tenant_id,
        kv.c.name)

    # Key-Value Items ----------------------------------------------
    kvitem = Table(
        "kv_items",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", BigInteger, primary_key=True, comment="Item ID"),
        Column(
            "kv_id", BigInteger, primary_key=True, comment="Key-Value Storage ID"),
        Column(
            "key", String(50), comment="Key-Value Storage Key"),
        Column(
            "value", String(500), nullable=False, comment="Key-Value Storage Value"),
        Column(
            "calculation", String(3), CheckConstraint("calculation = 'ADD' OR calculation = 'MOD' OR calculation = 'FN'", name="kv_items_chk_calculation"), nullable=False, comment="Calculation method"),
        Column(
            "typeof", String(10), nullable=True, comment="Type of value. E.g. 'json', 'string', 'int'"),
        UniqueConstraint("tenant_id", "kv_id", "key", name="kv_items_unk"),
        comment="KV Item can be assign to single one KVS"
    )
    set_version(kvitem)
    set_auditable(kvitem)
    Index(
        "ix_kv_items_001",
        kvitem.c.tenant_id,
        kvitem.c.kv_id,
        kvitem.c.key)
    Index(
        "ix_kv_items_002",
        kvitem.c.tenant_id,
        kvitem.c.kv_id)

    # Conditions ----------------------------------------------
    expression = Table(
        "conditions",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", BigInteger, primary_key=True, comment="Expression ID"),
        Column(
            "condition_id", BigInteger, primary_key=True, comment="Rule ID"),
        Column(
            "expression", String(1024), nullable=False, comment="Expression"),
        comment="A simple expression"
    )
    set_version(expression)
    set_auditable(expression)
    Index(
        "ix_expressions_001",
        expression.c.tenant_id,
        expression.c.condition_id)

    # Matrixes ----------------------------------------------
    case = Table(
        "cases",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", BigInteger, primary_key=True, comment="Expression ID"),
        Column(
            "rule_id", BigInteger, primary_key=True, comment="Rule ID"),
        Column(
            "position", Integer, nullable=False, comment="Position"),
        Column(
            "kvs_id_ok", BigInteger, nullable=True, comment="KVS associated when condition was successful"),
        Column(
            "kvs_id_nok", BigInteger, nullable=True, comment="KVS associated when condition was failed"),
        comment="A simple business case"
    )
    set_version(case)
    set_auditable(case)
    Index(
        "ix_cases_001",
        case.c.tenant_id,
        case.c.rule_id)

    # Rules ----------------------------------------------
    rule = Table(
        "rules",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", BigInteger, primary_key=True, comment="Rule ID"),
        Column(
            "name", String(50), nullable=False, unique=True, comment="Rule's Name"),
        Column(
            "rule_type", String(4), CheckConstraint("rule_type = 'CASE' OR rule_type = 'TREE'", name="rules_chk_rule_type"), nullable=False, comment="Type of Rule (SWITCH, IFELSE)"),
        Column(
            "kvs_id_nok", BigInteger, nullable=True, comment="KVS associated when no condition was success"),
        comment="A Rule is a simple business validation"
    )
    set_version(rule)
    set_auditable(rule)
    Index(
        "ix_rules_001",
        rule.c.tenant_id,
        rule.c.name)

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

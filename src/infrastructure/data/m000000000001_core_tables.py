""" migration file """

from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, Boolean
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
            "calculate", String(3), CheckConstraint("calculate = 'ADD' OR calculate = 'MOD'", name="kv_items_chk_calculate"), nullable=False, comment="Calculation method"),
        Column(
            "typeof", String(50), nullable=True, comment="Type of value. E.g. 'json', 'string', 'int'"),
        UniqueConstraint("tenant_id", "kv_id", "key", name="kv_items_unk"),
        comment="KV Item can be assign to single one KVS"
    )
    set_version(kvitem)
    set_auditable(kvitem)

    # Conditions ----------------------------------------------
    exp = Table(
        "conditions",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", BigInteger, primary_key=True, comment="Expression ID"),
        Column(
            "rule_id", BigInteger, primary_key=True, comment="Rule ID"),
        Column(
            "expression", String(1024), nullable=False, comment="Expression"),
        Column(
            "position", Integer, nullable=False, comment="Position"),
        Column(
            "operator", String(3), CheckConstraint("operator = 'AND' OR operator = 'OR'", name="conditions_chk_operator"), nullable=False, comment="Operator [OR, AND=default]"),
        comment="A simple business validation"
    )
    set_version(exp)
    set_auditable(exp)

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
            "is_zero_condition", Boolean, nullable=False, comment="Active force OK result"),
        Column(
            "kvs_id", BigInteger, nullable=True, comment="Linked KVS"),
        comment="A Rule is a simple business validation"
    )
    set_version(rule)
    set_auditable(rule)

    # Node ----------------------------------------------
    node = Table(
        "nodes",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "rule_id", BigInteger, primary_key=True, comment="Rule ID"),
        Column(
            "related_rule_id", BigInteger, primary_key=True, comment="Related Rule ID"),
        Column(
            "position", Integer, nullable=False, comment="Position Order"),
        comment="Nodes determine a rule connected to another ones"
    )
    set_version(node)
    set_auditable(node)

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
            "kvs_id_in", Boolean, comment="KVS ID used as input"),
        comment="Entrypoint determine which Rules will be called"
    )
    set_version(entrypoint)
    set_auditable(entrypoint)

    metadata_obj.create_all(engine)

    with Session(engine) as session:
        m = Migrations()
        m.id = name
        m.exec_date = datetime.now()
        session.add(m)
        session.commit()
        return name

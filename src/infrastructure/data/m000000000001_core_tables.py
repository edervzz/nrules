""" migration file """

from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, Boolean
from sqlalchemy import MetaData, Table,  CheckConstraint, Engine, select
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
        comment="KV Item can be assign to single one KVS"
    )
    set_version(kvitem)
    set_auditable(kvitem)

    # Expressions ----------------------------------------------
    exp = Table(
        "expressions",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", BigInteger, primary_key=True, comment="Expression ID"),
        Column(
            "expression", String(1024), nullable=False, comment="Expression"),
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
            "name", String(50), nullable=False, comment="Rule Name"),
        Column(
            "is_switch", BigInteger, nullable=True, comment="Rule work as switch"),
        Column(
            "rule_id", BigInteger, nullable=True, comment="Linked rule"),
        Column(
            "kvs_id", BigInteger, nullable=True, comment="Linked KVS"),
        comment="A Rule is a simple business validation"
    )
    set_version(rule)
    set_auditable(rule)

    # switches ----------------------------------------------
    switches = Table(
        "switches",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "rule_id", BigInteger, primary_key=True, comment="Rule ID"),
        Column(
            "rule_id1", BigInteger, primary_key=False, comment="Rule ID 1"),
        Column(
            "rule_id2", BigInteger, primary_key=False, comment="Rule ID 2"),
        Column(
            "rule_id3", BigInteger, primary_key=False, comment="Rule ID 3"),
        Column(
            "rule_id4", BigInteger, primary_key=False, comment="Rule ID 4"),
        Column(
            "rule_id5", BigInteger, primary_key=False, comment="Rule ID 5"),
        Column(
            "rule_id6", BigInteger, primary_key=False, comment="Rule ID 6"),
        Column(
            "rule_id7", BigInteger, primary_key=False, comment="Rule ID 7"),
        Column(
            "rule_id8", BigInteger, primary_key=False, comment="Rule ID 8"),
        Column(
            "rule_id9", BigInteger, primary_key=False, comment="Rule ID 9"),
        comment="9 exits"
    )
    set_version(switches)
    set_auditable(switches)

    # Entrypoint Storage ----------------------------------------------
    entrypoint = Table(
        "entrypoints",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", Integer, primary_key=True, comment="Entrypoint ID"),
        Column(
            "name", String(32), comment="Name code of Entrypoint"),
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

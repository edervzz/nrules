""" migration file """

from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String
from sqlalchemy import MetaData, Table,  CheckConstraint, Engine, select
from sqlalchemy.orm import Session
from domain.entities import Migrations
from .audit import set_auditable, set_version


def tables_base(engine: Engine):
    """000000000001_tables_base"""

    name = "000000000001_tables_base"

    metadata_obj = MetaData()

    stms = select(Migrations).where(Migrations.id == name)
    with Session(engine) as session:
        result = session.scalar(stms)
        if result is not None:
            return

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
            "key", String(50), primary_key=True, comment="Key-Value Storage Key"),
        Column(
            "kv_id", BigInteger, primary_key=True, comment="Key-Value Storage ID"),
        Column(
            "value", String(500), nullable=False, comment="Key-Value Storage Value"),
        Column(
            "typeof", String(50), nullable=True, comment="Type of value. E.g. 'json', 'string', 'int'"),
        comment="KV Item can be assign to single one KVS"
    )
    set_version(kvitem)
    set_auditable(kvitem)

    # Action ----------------------------------------------
    actions = Table(
        "actions",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", BigInteger, primary_key=True, comment="Key-Value Storage ID"),
        Column(
            "workflow_id", String(50), primary_key=True, comment="Key-Value Storage Key"),
        Column(
            "kvs_id", String(500), nullable=False, comment="Key-Value Storage Value"),
        comment="Actions determine to whom call or retrieve as result of rule or workflow."
    )
    set_version(actions)
    set_auditable(actions)

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
            "expression", String(1024), nullable=False, comment="Expression"),
        comment="A Rule is a simple business validation"
    )
    set_version(rule)
    set_auditable(rule)

    # Workflows ----------------------------------------------
    workflows = Table(
        "workflows",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", BigInteger, primary_key=True, comment="Workflow ID"),
        Column(
            "name", String(50), nullable=False, comment="Workflow Name"),
        Column(
            "typeof", String(4), CheckConstraint("typeof = 'BASE' OR typeof = 'FULL' OR typeof = 'NODE'", name="workflow_chk_typeof"), nullable=False,
            comment="Type of Workflow: Base, full, node"),
        Column(
            "action_id_ok", BigInteger, nullable=True, comment="Action to perform when result is success"),
        Column(
            "action_id_nok", BigInteger, nullable=True, comment="Action to perform when result is success"),
        comment="A Workflow can be performed as Node or call actions by result"
    )
    set_version(workflows)
    set_auditable(workflows)

    # Containers ----------------------------------------------
    container = Table(
        "containers",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "workflow_id", Integer, primary_key=True, comment="Workflow ID"),
        Column(
            "rule_id", Integer, primary_key=True, comment="Workflow ID"),
        Column(
            "operator", String(3), CheckConstraint("operator = 'AND' OR operator = 'OR'", name="container_rules_chk_operator"), nullable=False,
            comment="Operator evaluates rules between them. Only works when Workflow is type Base."),
        Column(
            "order", Integer, nullable=False, comment="Position into set of rules"),
        Column(
            "action_id_ok", BigInteger, nullable=True, comment="Action to perform when result is success. Only works when Workflow is type Node"),
        comment="Relation between Workflows and Rules. Can assign operator, order and success-action"
    )
    set_version(container)
    set_auditable(container)

    # Entrypoint Storage ----------------------------------------------
    entrypoint = Table(
        "entrypoints",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "key", String(32), primary_key=True, comment="Key of Entrypoint"),
        Column(
            "workflow_id", BigInteger, comment="Workflow ID"),
        comment="Entrypoint determine which workflow will be called"
    )
    set_version(entrypoint)
    set_auditable(entrypoint)

    # Variant Storage ----------------------------------------------
    variant = Table(
        "variants",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "key", String(32), primary_key=True, comment="Key"),
        Column(
            "entrypoint_key", String(32), primary_key=True, comment="Key of Entrypoint"),
        Column(
            "value", String(100), nullable=False, comment="Value"),
        comment="Variant is a container for many Key-Values"
    )
    set_version(variant)
    set_auditable(variant)

    metadata_obj.create_all(engine)

    with Session(engine) as session:
        m = Migrations()
        m.id = name
        m.exec_date = datetime.now()
        session.add(m)
        session.commit()

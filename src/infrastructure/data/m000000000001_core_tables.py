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
            "id", BigInteger, primary_key=True, comment="Action ID"),
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

    # ruleset ----------------------------------------------
    workflow = Table(
        "workflows",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", BigInteger, primary_key=True, comment="Workflow ID"),
        Column(
            "name", String(50), nullable=False, comment="workflow Name"),
        Column(
            "typeof", String(4), CheckConstraint("typeof = 'BASE' OR typeof = 'FULL' OR typeof = 'NODE'", name="workflows_chk_typeof"), nullable=False,
            comment="Type of workflow: Base, full, node"),
        Column(
            "action_id_ok", BigInteger, nullable=True, comment="Action to perform when result is success"),
        Column(
            "action_id_nok", BigInteger, nullable=True, comment="Action to perform when result is success"),
        comment="A Workflow can be performed as Node or call actions by result"
    )
    set_version(workflow)
    set_auditable(workflow)

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
            "id", Integer, primary_key=True, comment="Entrypoint ID"),
        Column(
            "name", String(32), comment="Name code of Entrypoint"),
        Column(
            "ruleset_id", BigInteger, comment="Rule Set ID"),
        Column(
            "is_active", Boolean, comment="Entrypoint is active"),
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
            "id", Integer, primary_key=True, comment="Variant ID"),
        Column(
            "entrypoint_id", Integer, primary_key=True, comment="ID of Entrypoint"),
        Column(
            "key", String(32), primary_key=True, comment="Key"),
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
        return name

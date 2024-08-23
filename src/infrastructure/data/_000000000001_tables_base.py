""" migration file """

from datetime import datetime
from sqlalchemy import Column, Boolean, Integer, BigInteger, String
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

    # Variant Storage ----------------------------------------------
    variant = Table(
        "variant",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", BigInteger, primary_key=True, comment="Variant ID"),
        Column(
            "name", String(50), nullable=False, comment="Variant Name", unique=True),
        Column(
            "values", String(2000), nullable=False, comment="Values"),
        comment="Variant is a container for many Key-Values"
    )
    set_version(variant)
    set_auditable(variant)

    # Workflows ----------------------------------------------
    workflows = Table(
        "workflows",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", BigInteger, primary_key=True, comment="Workflow ID"),
        Column(
            "name", String(50), nullable=False, comment="Workflow Name", unique=True),
        Column(
            "variant_id", BigInteger, comment="Variant ID"),
        Column(
            "container_id", BigInteger, comment="Container ID"),
        Column(
            "workflow_id_ok", BigInteger, nullable=True, comment="Workflow ID to perform when result is success"),
        Column(
            "kv_id_ok", BigInteger, nullable=True, comment="Key-Value Storage ID to collect when result is success"),
        Column(
            "workflow_id_nok", BigInteger, nullable=True, comment="Workflow ID to perform when result is success"),
        Column(
            "kv_id_nok", BigInteger, nullable=True, comment="Key-Value Storage ID to collect when result is success"),
        comment="A Workflow can be performed as Node or call actions by result"
    )
    set_version(workflows)
    set_auditable(workflows)

    # Rules ----------------------------------------------
    rule = Table(
        "rules",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", BigInteger, primary_key=True, comment="Rule ID"),
        Column(
            "name", String(50), nullable=False, comment="Rule Name", unique=True),
        Column(
            "expression", String(1024), nullable=False, comment="Expression"),
        Column(
            "is_exclusive", Boolean, nullable=False, comment="Set Rule as exclusive to current workflow(s). Default: false"),
        comment="A Rule is a simple business validation"
    )
    set_version(rule)
    set_auditable(rule)

    # Containers ----------------------------------------------
    container = Table(
        "containers",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", Integer, primary_key=True, comment="Container ID"),
        Column(
            "name", String(50), nullable=False, comment="Container Name", unique=True),
        Column(
            "is_node", Boolean, comment="Container is a Node. Container works like decision node via Rules depending of Rule's Order"),
        Column(
            "is_full", Boolean, comment="Every Rule is evaluated independently, workflow returns a list of results and actions"),
        comment="Relation between Workflows and Rules. Can assign operator, order and success-action"
    )
    set_version(container)
    set_auditable(container)

    # Container Rules ----------------------------------------------
    container_rules = Table(
        "container_rules",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "container_id", Integer, primary_key=True, comment="Container ID"),
        Column(
            "rule_id", BigInteger, primary_key=True, nullable=False, comment="Rule ID"),
        Column(
            "operator", String(3), CheckConstraint("operator = 'AND' OR operator = 'OR'", name="container_rules_chk_operator"), nullable=False,
            comment="Operator evaluates rules between them. Only works when Container when it is neither Node nor Full."),
        Column(
            "order", Integer, nullable=False, comment="Order"),
        Column(
            "workflow_id_ok", BigInteger, nullable=True, comment="Workflow ID to perform when result is success"),
        Column(
            "kv_id_ok", BigInteger, nullable=True, comment="Key-Value Storage ID to collect when result is success"),
        comment="Relation between Workflows and Rules. Can assign operator, order and success-action"
    )
    set_version(container_rules)
    set_auditable(container_rules)

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
            "kv_id", BigInteger, primary_key=True, comment="Key-Value Storage ID"),
        Column(
            "key", String(50), primary_key=True, comment="Key-Value Storage Key"),
        Column(
            "value", String(500), nullable=False, comment="Key-Value Storage Value"),
        Column(
            "type_value", String(50), nullable=True, comment="Type of value. E.g. 'json', 'string', 'int'"),
        comment="KV Item can be assign to single one KVS"
    )
    set_version(kvitem)
    set_auditable(kvitem)

    metadata_obj.create_all(engine)

    with Session(engine) as session:
        m = Migrations()
        m.id = name
        m.exec_date = datetime.now()
        session.add(m)
        session.commit()

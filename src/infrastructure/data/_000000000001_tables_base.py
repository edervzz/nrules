""" migration file """

from datetime import datetime
from sqlalchemy import Column, Boolean, Integer, BigInteger, String
from sqlalchemy import MetaData, Table,  CheckConstraint, Engine, select
from sqlalchemy.orm import Session
from domain.entities import Migrations
from .audit import set_auditable


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
            "id", BigInteger, primary_key=True, autoincrement=True, comment="Variant ID"),
        Column(
            "name", String(50), nullable=False, comment="Variant Name", unique=True),
        Column(
            "values", String(2000), nullable=False, comment="Values"),
        comment="Variant is a container for many Key-Values"
    )
    set_auditable(variant)

    # Workflows ----------------------------------------------
    workflows = Table(
        "workflows",
        metadata_obj,
        Column(
            "id", BigInteger, primary_key=True, autoincrement=True, comment="Workflow ID"),
        Column(
            "name", String(50), nullable=False, comment="Workflow Name", unique=True),
        Column(
            "variant_id", BigInteger, comment="Variant ID"),
        Column(
            "is_node", Boolean, comment="Workflow is a Node. Workflow works like decision node via Rules depending of Rule's Order"),
        Column(
            "is_parcial", Boolean, comment="Final Result is Parcial. Every Rule is evaluated independently, workflow returns a list of results and action"),
        Column(
            "action_on_success", BigInteger, comment="Call an Action for success result by ID"),
        Column(
            "action_on_failure", BigInteger, comment="Call an Action for failure result by ID"),
        comment="A Workflow can be performed as Node or call actions by result"
    )
    set_auditable(workflows)

    # Rules ----------------------------------------------
    rule = Table(
        "rules",
        metadata_obj,
        Column(
            "id", BigInteger, primary_key=True, autoincrement=True, comment="Rule ID"),
        Column(
            "name", String(50), nullable=False, comment="Rule Name", unique=True),
        Column(
            "expression", String(1024), nullable=False, comment="Expression"),
        Column(
            "is_exclusive", Boolean, nullable=False, comment="Set Rule as exclusive to current workflow(s). Default: false"),
        comment="A Rule is a simple business validation"
    )
    set_auditable(rule)

    # Workflow Rules ----------------------------------------------
    workflow_rule = Table(
        "workflows_rules",
        metadata_obj,
        Column(
            "workflow_id", BigInteger, primary_key=True, nullable=False, comment="Workflow ID"),
        Column(
            "rule_id", BigInteger, primary_key=True, nullable=False, comment="Rule ID"),
        Column(
            "operator", String(3), CheckConstraint("operator = 'AND' OR operator = 'OR'", name="rules_chk_operator"), nullable=False, comment="Operator"),
        Column(
            "order", Integer, nullable=True, comment="Order"),
        Column(
            "action_on success", BigInteger, comment="Call an Action for success result by ID"),
        comment="Relation between Workflows and Rules. Can assign operator, order and success-action"
    )
    set_auditable(workflow_rule)

    # Key-Value Storage ----------------------------------------------
    kv = Table(
        "kvs",
        metadata_obj,
        Column(
            "id", BigInteger, primary_key=True, autoincrement=True, comment="Key-Value Storage ID"),
        Column(
            "name", String(50), nullable=False, comment="Key-Value Storage Name", unique=True),
        comment="KVS is a container for many Key-Values"
    )
    set_auditable(kv)

    # Key-Value Items ----------------------------------------------
    kvitem = Table(
        "kv_items",
        metadata_obj,
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
    set_auditable(kvitem)

    # Actions ----------------------------------------------
    actions = Table(
        "actions",
        metadata_obj,
        Column(
            "id", BigInteger, primary_key=True, autoincrement="auto", comment="Action ID"),
        Column(
            "name", String(50), nullable=False, comment="Action Name", unique=True),
        Column(
            "workflow_id", BigInteger, primary_key=True, autoincrement=True, comment="Workflow ID to perform"),
        Column(
            "kv_id", BigInteger, primary_key=True, comment="Key-Value Storage ID to collect"),
        comment="An Action can perform a Workflor or KVS. It can be assign to Rules or Workflows"
    )
    set_auditable(actions)

    metadata_obj.create_all(engine)

    with Session(engine) as session:
        m = Migrations()
        m.id = name
        m.exec_date = datetime.now()
        session.add(m)
        session.commit()

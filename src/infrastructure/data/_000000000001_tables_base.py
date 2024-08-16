""" migration file """

from datetime import datetime
from sqlalchemy import Column, Boolean, Integer, BigInteger, String
from sqlalchemy import MetaData, Table,  CheckConstraint, Engine, select
from sqlalchemy.orm import Session
from domain.entities import Migrations
from .audit import set_auditable


def tables_base(engine: Engine):
    """_summary_ """

    name = "000000000001_tables_base"

    metadata_obj = MetaData()

    stms = select(Migrations).where(Migrations.id == name)
    with Session(engine) as session:
        result = session.scalar(stms)
        if result is not None:
            return

    workflow_rule = Table(
        "workflow_rules",
        metadata_obj,
        Column(
            "workflow_id", BigInteger, primary_key=True, nullable=False, comment="Workflow ID."),
        Column(
            "rule_id", BigInteger, primary_key=True, nullable=False, comment="Rule ID.")
    )
    set_auditable(workflow_rule)

    rule = Table(
        "rules",
        metadata_obj,
        Column(
            "id", BigInteger, primary_key=True, autoincrement=True, comment="Rule ID."),
        Column(
            "name", String(50), nullable=False, comment="Rule Name.", unique=True),
        Column(
            "operator", String(3), CheckConstraint("operator = 'AND' OR operator = 'OR'", name="rules_chk_operator"), nullable=True, comment="Operator."),
        Column(
            "expression", String(1024), nullable=False, comment="Expression."),
        Column(
            "order", Integer, nullable=True, comment="Order."),
        Column(
            "is_multi_assignment", Boolean, nullable=False, comment="Can be assign to multiple Workflows. Default: false.")
    )
    set_auditable(rule)

    workflows = Table(
        "workflows",
        metadata_obj,
        Column(
            "id", BigInteger, primary_key=True, autoincrement=True, comment="Workflow ID."),
        Column(
            "name", String(50), nullable=False, comment="Workflow Name.", unique=True),
        Column(
            "is_node", Boolean, comment="Workflow works likes decision node."),
        Column(
            "variant_id", BigInteger, comment="Variant ID."),
        Column(
            "success_action_id", BigInteger, comment="Action ID for success result."),
        Column(
            "failure_action_id", BigInteger, comment="Action ID for failure result."),
    )
    set_auditable(workflows)

    metadata_obj.create_all(engine)

    with Session(engine) as session:
        m = Migrations()
        m.id = name
        m.exec_date = datetime.now()
        session.add(m)
        session.commit()

""" migration file """
from sqlalchemy import MetaData, Table, Column, Boolean, Integer, BigInteger, String, CheckConstraint
from .m_000000000001_init import set_auditable


def tables(metadata_obj: MetaData):
    """_summary_

    Args:
        metadata_obj (MetaData): _description_
    """
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

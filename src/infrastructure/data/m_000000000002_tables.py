""" migration file """
from sqlalchemy import MetaData, Table, Column, Boolean, BigInteger, String, CheckConstraint
from .m_000000000001_init import set_auditable


def tables(metadata_obj: MetaData):
    """_summary_

    Args:
        metadata_obj (MetaData): _description_
    """
    workflows = Table(
        "workflows",
        metadata_obj,
        Column("id", BigInteger, primary_key=True,
               autoincrement=True, comment="Workflow ID."),
        Column("name", String(50), nullable=False,
               comment="Workflow Name.", unique=True),
        Column("is_node", Boolean, comment="Workflow works likes decision node."),
        Column("variant_id", BigInteger, comment="Variant ID."),
        Column("success_action_id", BigInteger,
               comment="Action ID for success result."),
        Column("failure_action_id", BigInteger,
               comment="Action ID for failure result."),
    )

    set_auditable(workflows)

    rule = Table(
        "rules",
        metadata_obj,
        Column("id", BigInteger, primary_key=True,
               autoincrement=True, comment="Workflow ID."),
        Column("name", String(50), nullable=False,
               comment="Rule Name.", unique=True),
        Column("operator", String(3), CheckConstraint(
            "operator = 'AND' OR operator = 'OR'", name="rules_chk_operator"), comment="Operator."),
        Column("expression", String(1024), comment="Variant ID.")
    )

    set_auditable(rule)

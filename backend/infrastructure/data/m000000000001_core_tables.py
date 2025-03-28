""" migration file """
from datetime import datetime
from sqlalchemy import Column, Integer, String, Index, Boolean, ForeignKeyConstraint
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

    # Rules ----------------------------------------------
    rule = Table(
        "rules",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", String(36), primary_key=True, comment="Rule ID"),
        Column(
            "name", String(50), nullable=False, unique=True, comment="Rule's Name"),
        Column(
            "rule_type", String(6), CheckConstraint("rule_type = 'TABLE' OR rule_type = 'TREE'", name="rules_chk_rule_type"), nullable=False, comment="Type of Rule (TABLE, TREE)"),
        Column(
            "strategy", String(5), CheckConstraint("strategy = 'EARLY' OR strategy = 'BASE' OR strategy = 'ALL'", name="rules_chk_strategy"), nullable=False, comment="Strategy of rule depending of Type"),
        Column(
            "is_check", Boolean, nullable=False, comment="Rule is Checked"),
        Column(
            "is_active", Boolean, nullable=False, comment="Rule is Active"),
        Column(
            "is_archived", Boolean, nullable=False, comment="Rule is Archived"),
        comment="Rule Catalog"
    )
    set_version(rule)
    set_auditable(rule)
    Index(
        "ix_rules_001",
        rule.c.tenant_id,
        rule.c.name)

    # Parameters ----------------------------------------------
    parameters = Table(
        "parameters",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "key", String(50), primary_key=True, comment="Paramater Key"),
        Column(
            "rule_id", String(36), primary_key=True, comment="Rule ID"),
        Column(
            "usefor", String(10), CheckConstraint("usefor = 'INPUT' OR usefor = 'OUTPUT'", name="parameters_chk_usefor"), primary_key=True, comment="Use for: INPUT, OUTPUT"),
        Column(
            "typeof", String(10), CheckConstraint("typeof = 'JSON' OR typeof = 'STRING' OR typeof = 'NUMERIC' OR typeof = 'DATE' OR typeof = 'TIME' OR typeof = 'DATETIME'", name="parameters_chk_typeof"), nullable=False, comment="Type of Value: String, Numeric, Date"),
        Column(
            "is_active", Boolean, nullable=False, comment="Parameter is active"),
        Column(
            "is_archived", Boolean, nullable=False, comment="Parameter is archived"),
        ForeignKeyConstraint(
            ["tenant_id", "rule_id"], ["rules.tenant_id", "rules.id"]),
        comment="Control which parameters serve as input and output"
    )
    set_auditable(parameters)
    Index(
        "ix_parameters_001",
        parameters.c.rule_id)

    # Cases ----------------------------------------------
    cases = Table(
        "cases",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", String(36), primary_key=True, comment="ID"),
        Column(
            "rule_id", String(36), comment="Rule ID"),
        Column(
            "position", Integer, CheckConstraint("position > 0", name="cases_chk_position"), nullable=False, comment="Position"),
        Column(
            "is_active", Boolean, nullable=False, comment="Case is Active"),
        Column(
            "is_archived", Boolean, nullable=False, comment="Case is Archived"),
        ForeignKeyConstraint(
            ["tenant_id", "rule_id"], ["rules.tenant_id", "rules.id"]),
        comment="Cases. Set execution order"
    )
    set_auditable(cases)
    Index(
        "ix_cases_001",
        cases.c.tenant_id,
        cases.c.rule_id)

    # Conditions  ----------------------------------------------
    conditions = Table(
        "conditions",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "variable", String(50), primary_key=True, comment="Variable Name"),
        Column(
            "case_id", String(36), primary_key=True, comment="Case ID"),
        Column(
            "rule_id", String(36), comment="Rule ID"),
        Column(
            "operator", String(10), nullable=False, comment="Operator"),
        Column(
            "value", String(50), nullable=False, comment="Value"),
        ForeignKeyConstraint(
            ["tenant_id", "rule_id"], ["rules.tenant_id", "rules.id"]),
        ForeignKeyConstraint(
            ["tenant_id", "case_id"], ["cases.tenant_id", "cases.id"]),
        comment="Matrix's Columns. Set expressions to evaluate"
    )
    set_auditable(conditions)
    Index(
        "ix_conditions_001",
        conditions.c.rule_id)

    # Key-Value Items ----------------------------------------------
    kvitems = Table(
        "kv_items",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "key", String(50), primary_key=True, comment="Key"),
        Column(
            "case_id", String(36),  primary_key=True, comment="Case ID"),
        Column(
            "rule_id", String(36),  nullable=False, comment="Rule ID"),
        Column(
            "value", String(500), nullable=False, comment="Value"),
        Column(
            "calculation", String(3), CheckConstraint("calculation = 'ADD' OR calculation = 'MOD' OR calculation = 'FN'", name="kv_items_chk_calculation"), nullable=True, comment="Calculation method"),
        ForeignKeyConstraint(
            ["tenant_id", "rule_id"], ["rules.tenant_id", "rules.id"]),
        ForeignKeyConstraint(
            ["tenant_id", "case_id"], ["cases.tenant_id", "cases.id"]),
        comment="KV Item can be assign to single one KVS"
    )
    set_auditable(kvitems)
    Index(
        "ix_kv_items_001",
        kvitems.c.rule_id)
    Index(
        "ix_kv_items_002",
        kvitems.c.tenant_id,
        kvitems.c.case_id)

    # Node ----------------------------------------------
    node = Table(
        "nodes",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", String(36), primary_key=True, comment="ID"),
        Column(
            "rule_id", String(36), primary_key=True, comment="Rule ID"),
        Column(
            "case_id", String(36), primary_key=True, comment="Case ID"),
        Column(
            "left_node_id", String(36), nullable=True, comment="Left Node ID"),
        Column(
            "right_node_id", String(36), nullable=True, comment="Right Node ID"),
        Column(
            "is_active", Boolean, nullable=False, comment="Case is Active"),
        Column(
            "is_archived", Boolean, nullable=False, comment="Case is Archived"),
        ForeignKeyConstraint(
            ["tenant_id", "rule_id"], ["rules.tenant_id", "rules.id"]),
        ForeignKeyConstraint(
            ["tenant_id", "case_id"], ["cases.tenant_id", "cases.id"]),
        comment="Cases. Set execution order"
    )
    set_auditable(node)
    Index(
        "ix_cases_001",
        node.c.tenant_id,
        node.c.rule_id)

    # Tags ----------------------------------------------
    tags = Table(
        "tags",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "rule_id", String(36), primary_key=True, comment="Rule ID"),
        Column(
            "key", String(50), primary_key=True, nullable=False, comment="Tag's key"),
        Column(
            "value", String(80), nullable=False, comment="Value"),
        ForeignKeyConstraint(
            ["tenant_id", "rule_id"], ["rules.tenant_id", "rules.id"]),
        comment="Tags Catalog"
    )
    set_auditable(tags)
    Index(
        "ix_tags_001",
        tags.c.rule_id)

    metadata_obj.create_all(engine)

    with Session(engine) as session:
        m = Migrations()
        m.id = name
        m.exec_date = datetime.now()
        session.add(m)
        session.commit()
        return name

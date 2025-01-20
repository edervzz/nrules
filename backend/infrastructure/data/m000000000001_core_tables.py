""" migration file """
from datetime import datetime
from sqlalchemy import Column, Integer, String, Index, Boolean
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

    # Key-Value Items ----------------------------------------------
    kvitems = Table(
        "kv_items",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "key", String(50), primary_key=True, comment="Key"),
        Column(
            "case_id", String(36), primary_key=True, comment="Case ID"),
        Column(
            "rule_id", String(36), primary_key=False, comment="Rule ID"),
        Column(
            "value", String(500), nullable=False, comment="Value"),
        Column(
            "calculation", String(3), CheckConstraint("calculation = 'ADD' OR calculation = 'MOD' OR calculation = 'FN'", name="kv_items_chk_calculation"), nullable=True, comment="Calculation method"),
        UniqueConstraint("tenant_id", "case_id", "key", name="kv_items_unk"),
        comment="KV Item can be assign to single one KVS"
    )
    set_auditable(kvitems)
    Index(
        "ix_kv_items_001",
        kvitems.c.tenant_id,
        kvitems.c.case_id)

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
            "rule_type", String(6), CheckConstraint("rule_type = 'MATRIX' OR rule_type = 'TREE'", name="rules_chk_rule_type"), nullable=False, comment="Type of Rule (MATRIX, TREE)"),
        Column(
            "strategy", String(5), CheckConstraint("strategy = 'EARLY' OR strategy = 'BASE' OR strategy = 'ALL'", name="rules_chk_strategy"), nullable=False, comment="Strategy of rule depending of Type"),
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
        comment="Rule Catalog"
    )
    set_auditable(tags)

    # Cases ----------------------------------------------
    cases = Table(
        "cases",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", String(36), primary_key=True, comment="ID"),
        Column(
            "rule_id", String(36), primary_key=True, comment="Rule ID"),
        Column(
            "position", Integer, nullable=False, comment="Position"),
        Column(
            "is_active", Boolean, nullable=False, comment="Case is Active"),
        Column(
            "is_archived", Boolean, nullable=False, comment="Case is Archived"),
        comment="Matrix's Rows. Set execution order"
    )
    set_auditable(cases)
    Index(
        "ix_cases_001",
        cases.c.tenant_id,
        cases.c.rule_id)

    # conditions  ----------------------------------------------
    conditions = Table(
        "conditions",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "variable", String(50), primary_key=True, nullable=False, comment="Variable Name"),
        Column(
            "case_id", String(36), primary_key=True, comment="Case ID"),
        Column(
            "rule_id", String(36), primary_key=False, comment="Rule ID"),
        Column(
            "operator", String(10), nullable=False, comment="Operator"),
        Column(
            "value", String(50), nullable=False, comment="Value"),
        comment="Matrix's Columns. Set expressions to evaluate"
    )
    set_auditable(conditions)

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
        comment="Control which parameters serve as input and output"
    )
    set_auditable(parameters)
    Index(
        "ix_parameters_001",
        parameters.c.rule_id)

    metadata_obj.create_all(engine)

    with Session(engine) as session:
        m = Migrations()
        m.id = name
        m.exec_date = datetime.now()
        session.add(m)
        session.commit()
        return name

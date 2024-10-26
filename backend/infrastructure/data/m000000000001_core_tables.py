""" migration file """
from datetime import datetime
from sqlalchemy import Column, Integer, String, Index
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

    # Key-Value Storage ----------------------------------------------
    kvs = Table(
        "kvs",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", String(36), primary_key=True, comment="Key-Value Storage ID"),
        comment="KVS is a container for many Key-Values"
    )
    set_auditable(kvs)

    # Key-Value Items ----------------------------------------------
    kvitems = Table(
        "kv_items",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "key", String(50), primary_key=True, comment="Key"),
        Column(
            "kv_id", String(36), primary_key=True, comment="Key-Value Storage ID"),
        Column(
            "value", String(500), nullable=False, comment="Value"),
        Column(
            "calculation", String(3), CheckConstraint("calculation = 'ADD' OR calculation = 'MOD' OR calculation = 'FN'", name="kv_items_chk_calculation"), nullable=True, comment="Calculation method"),
        Column(
            "typeof", String(10), nullable=True, comment="Type of value. E.g. 'json', 'string', 'int'"),
        UniqueConstraint("tenant_id", "kv_id", "key", name="kv_items_unk"),
        comment="KV Item can be assign to single one KVS"
    )
    set_auditable(kvitems)
    Index(
        "ix_kv_items_001",
        kvitems.c.tenant_id,
        kvitems.c.kv_id)

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
            "kvs_id_nok", String(36), nullable=True, comment="KVS associated when no condition was success"),
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
            "usefor", String(10), CheckConstraint("usefor = 'CONDITION' OR usefor = 'OUTPUT'", name="parameters_chk_usefor"), nullable=False, comment="Use for: CONDITION, OUTPUT"),
        Column(
            "typeof", String(10), nullable=False, comment="Type of Value: String, Numeric, Date"),
        comment="Extra information for expressions"
    )
    set_auditable(parameters)
    Index(
        "ix_parameters_001",
        parameters.c.rule_id)

    # Conditions ----------------------------------------------
    conditions = Table(
        "conditions",
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
            "parent_id", Integer, nullable=True, comment="Condition Parent ID"),
        Column(
            "kvs_id_ok", String(36), nullable=True, comment="KVS associated when condition was successful"),
        Column(
            "kvs_id_nok", String(36), nullable=True, comment="KVS associated when condition was failed"),
        comment="Matrix's Rows. Set execution order"
    )
    set_auditable(conditions)
    Index(
        "ix_conditions_001",
        conditions.c.tenant_id,
        conditions.c.rule_id)
    Index(
        "ix_conditions_002",
        conditions.c.tenant_id,
        conditions.c.parent_id)

    # Expressions  ----------------------------------------------
    expressions = Table(
        "expressions",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "id", String(36), primary_key=True, comment="ID"),
        Column(
            "condition_id", String(36), primary_key=True, comment="Condition ID"),
        Column(
            "variable", String(50), nullable=False, comment="Variable Name"),
        Column(
            "operator", String(10), nullable=False, comment="Operator"),
        Column(
            "value", String(50), nullable=False, comment="Value"),
        Column(
            "typeof", String(10), nullable=False, comment="Type of Value"),
        UniqueConstraint(
            "tenant_id", "id", name="kv_expressions_unk"),
        comment="Matrix's Columns. Set expressions to evaluate"
    )
    set_auditable(expressions)
    Index(
        "ix_expressions_001",
        expressions.c.tenant_id,
        expressions.c.condition_id)

    metadata_obj.create_all(engine)

    with Session(engine) as session:
        m = Migrations()
        m.id = name
        m.exec_date = datetime.now()
        session.add(m)
        session.commit()
        return name

""" migration file """

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
            "id", String(32), primary_key=True, comment="Key-Value Storage ID"),
        comment="KVS is a container for many Key-Values"
    )
    set_version(kvs)
    set_auditable(kvs)
    Index(
        "ix_kvs_001",
        kvs.c.tenant_id,
        kvs.c.name)

    # Key-Value Items ----------------------------------------------
    kvitems = Table(
        "kv_items",
        metadata_obj,
        Column(
            "tenant_id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "key", String(50), comment="Key"),
        Column(
            "kv_id", String(32), primary_key=True, comment="Key-Value Storage ID"),
        Column(
            "value", String(500), nullable=False, comment="Value"),
        Column(
            "calculation", String(3), CheckConstraint("calculation = 'ADD' OR calculation = 'MOD' OR calculation = 'FN'", name="kv_items_chk_calculation"), nullable=False, comment="Calculation method"),
        Column(
            "typeof", String(10), nullable=True, comment="Type of value. E.g. 'json', 'string', 'int'"),
        UniqueConstraint("tenant_id", "kv_id", "key", name="kv_items_unk"),
        comment="KV Item can be assign to single one KVS"
    )
    set_version(kvitems)
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
            "id", String(32), primary_key=True, comment="Rule ID"),
        Column(
            "name", String(50), nullable=False, unique=True, comment="Rule's Name"),
        Column(
            "rule_type", String(4), CheckConstraint("rule_type = 'MATRIX' OR rule_type = 'TREE'", name="rules_chk_rule_type"), nullable=False, comment="Type of Rule (MATRIX, TREE)"),
        Column(
            "strategy", String(4), CheckConstraint("strategy = 'EARLY' OR strategy = 'BASE' OR strategy = 'ALL'", name="rules_chk_rule_type"), nullable=False, comment="Strategy of rule depending of Type"),
        Column(
            "kvs_id_nok", String(32), nullable=True, comment="KVS associated when no condition was success"),
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
            "rule_id", String(32), primary_key=True, comment="Rule ID"),
        Column(
            "value_type", String(10), nullable=False, comment="Type of Value: String, Numeric, Date"),
        comment="Extra information for expressions"
    )
    set_version(parameters)
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
            "id", String(32), primary_key=True, comment="ID"),
        Column(
            "rule_id", String(32), primary_key=True, comment="Rule ID"),
        Column(
            "position", Integer, nullable=False, comment="Position"),
        Column(
            "parent_id", Integer, nullable=True, comment="Condition Parent ID"),
        Column(
            "kvs_id_ok", String(32), nullable=True, comment="KVS associated when condition was successful"),
        Column(
            "kvs_id_nok", String(32), nullable=True, comment="KVS associated when condition was failed"),
        comment="Matrix's Rows. Set execution order"
    )
    set_version(conditions)
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
            "id", String(32), primary_key=True, comment="ID"),
        Column(
            "condition_id", String(32), primary_key=True, comment="Condition ID"),
        Column(
            "expression", String(500), nullable=False, comment="Expression"),
        UniqueConstraint(
            "tenant_id", "id", name="kv_expressions_unk"),
        comment="Matrix's Columns. Set expressions to evaluate"
    )
    set_version(expressions)
    set_auditable(expressions)
    Index(
        "ix_expressions_001",
        expressions.c.tenant_id,
        expressions.c.condition_id)

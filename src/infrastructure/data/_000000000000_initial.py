""" migration file """

from sqlalchemy import Column, String, DateTime, Integer, BigInteger
from sqlalchemy import MetaData, Table,  Engine
from .audit import set_auditable


def initial(engine: Engine):
    """_summary_ """

    metadata_obj = MetaData()

    Table(
        "__migrations",
        metadata_obj,
        Column(
            "id", String(50), primary_key=True, comment="Migration ID"),
        Column(
            "exec_date", DateTime, nullable=False, comment="Execution Date"),
        comment="Save migrations previously executed."
    )

    # XObject Storage ----------------------------------------------
    variant = Table(
        "xobjects",
        metadata_obj,
        Column(
            "id", BigInteger, primary_key=True, autoincrement=True, comment="ID for Variants, Rules, Workflow, Actions, KVS"),
        Column(
            "object_name", String(50), nullable=False, comment="Variants / Rules / Workflows / Actions / KVS"),
        comment="Variant is a container for many Key-Values"
    )
    set_auditable(variant)

    # Tenant Storage ----------------------------------------------
    tenants = Table(
        "tenants",
        metadata_obj,
        Column(
            "id", Integer, primary_key=True, comment="Tenant ID"),
        Column(
            "name", String(60), nullable=False, comment="Tenant Name", unique=True),
        comment="Tenancy Storage"
    )
    set_auditable(tenants)

    # Tenant Stage Storage ----------------------------------------------
    tenants_stage = Table(
        "tenant_stages",
        metadata_obj,
        Column(
            "tenant_dev_id", Integer, primary_key=True, comment="Tenant Development ID"),
        Column(
            "tenant_test_id", Integer, comment="Tenant Testing ID"),
        Column(
            "tenant_release_id", Integer, comment="Tenant Release ID"),
        comment="Tenancy Storage"
    )
    set_auditable(tenants_stage)

    metadata_obj.create_all(engine)

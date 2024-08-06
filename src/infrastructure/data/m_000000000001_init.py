""" migration file """
from sqlalchemy import MetaData, Table, Column, String, DateTime


def migrations(metadata_obj: MetaData):
    """_summary_

    Args:
        metadata_obj (MetaData): _description_
    """
    Table(
        "__migrations",
        metadata_obj,
        Column("id", String(50), primary_key=True, comment="Migration ID."),
        Column("exec_date", DateTime, nullable=False,
               comment="Execution Date."),
    )


def set_auditable(table: Table):
    """ Add auditable columns

    Args:
        t (Table): table to add auditable columns
    """
    table.append_column(
        Column("created_by", String(50), comment="Created At."),
    )
    table.append_column(
        Column("created_at", DateTime, comment="Created At."),

    )
    table.append_column(
        Column("updated_by", String(50), comment="Created At."),

    )
    table.append_column(
        Column("updated_at", DateTime, comment="Created At."),
    )

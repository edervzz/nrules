""" migration file """
from sqlalchemy import Table, Column, String, DateTime


def set_auditable(table: Table):
    """ Add auditable columns

    Args:
        t (Table): table to add auditable columns
    """
    table.append_column(
        Column("created_by", String(50), comment="Created By", nullable=False),
    )
    table.append_column(
        Column("created_at", DateTime, comment="Created At", nullable=False),

    )
    table.append_column(
        Column("updated_by", String(50), comment="Updated By", nullable=False),

    )
    table.append_column(
        Column("updated_at", DateTime, comment="Updated At", nullable=False),
    )
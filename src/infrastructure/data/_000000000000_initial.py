""" migration file """

from sqlalchemy import Column, String, DateTime
from sqlalchemy import MetaData, Table,  Engine


def initial(engine: Engine):
    """_summary_ """

    metadata_obj = MetaData()

    Table(
        "__migrations",
        metadata_obj,
        Column(
            "id", String(50), primary_key=True, comment="Migration ID."),
        Column(
            "exec_date", DateTime, nullable=False, comment="Execution Date."),
    )

    metadata_obj.create_all(engine)

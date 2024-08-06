""" for testing purpose """

from sqlalchemy import create_engine, MetaData
from infrastructure import migrations, tables
from sqlalchemy.orm import Session
from domain.entities.workflow import Workflow


engine = create_engine(
    "mysql+pymysql://root:my-secret-pw@localhost/nrule-core", echo=True)

metadata_obj = MetaData()

migrations(metadata_obj=metadata_obj)
tables(metadata_obj)

metadata_obj.create_all(engine)

with Session(engine) as session:
    wf = Workflow()
    wf.name = "WF_test"
    # wf.variant_id = 0
    # wf.is_node = False
    # wf.success_action_id = 0
    # wf.failure_action_id = 0

    session.add(wf)
    session.commit()

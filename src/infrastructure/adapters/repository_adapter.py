"""_summary_
    """
from sqlalchemy import Engine, MetaData, create_engine, select
from sqlalchemy.orm import Session
from domain.entities import Workflow
from domain.ports import Repository
from infrastructure.data import migrations, tables


class RepositoryAdapter(Repository):
    """ Repository Adapter """

    def __init__(self, username: str, password: str, server: str, dbname: str):
        self.session: Session = None
        self.engine: Engine = create_engine(
            f"mysql+pymysql://{username}:{
                password}@{server}/{dbname}", echo=True
        )

    def create(self, entity: any):
        if isinstance(entity, list):
            for e in entity:
                self.session.add(e)
        else:
            self.session.add(entity)

    def workflow_read_by_external_id(self, external_id: str) -> Workflow:
        with Session(self.engine) as session:
            stmt = select(Workflow).where(Workflow.name == external_id)
            workflow = session.scalar(stmt)
            return workflow

    def begin(self):
        self.session = Session(self.engine)

    def commit_work(self):
        if self.session is not None:
            self.session.commit()

    def rollback_work(self):
        if self.session is not None:
            self.session.rollback()

    def migrate(self):
        metadata_obj = MetaData()
        migrations(metadata_obj=metadata_obj)
        tables(metadata_obj)

        metadata_obj.create_all(self.engine)

        with Session(self.engine) as session:
            wf = Workflow()
            wf.name = "WF_test"
            # wf.variant_id = 0
            # wf.is_node = False
            # wf.success_action_id = 0
            # wf.failure_action_id = 0

            session.add(wf)
            session.commit()

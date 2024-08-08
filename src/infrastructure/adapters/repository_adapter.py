"""_summary_
    """
from sqlalchemy import Engine, create_engine, select
from sqlalchemy.orm import Session
from domain.entities import Workflow
from domain.ports import Repository


class RepositoryAdapter(Repository):
    """ Repository Adapter """

    def __init__(self, username: str, password: str, server: str, dbname: str):
        self.username = username
        self.password = password
        self.server = server
        self.dbname = dbname

        self.session: Session = None
        self.engine: Engine = create_engine(
            f"mysql+pymysql://{self.username}:{
                self.password}@{self.server}/{self.dbname}",
            echo=True)

    def create(self, entity: any):
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

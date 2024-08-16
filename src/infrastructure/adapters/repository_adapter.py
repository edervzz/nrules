"""_summary_
    """
from typing import List
from datetime import datetime
from sqlalchemy import Engine, create_engine, select, event
from sqlalchemy.orm import Session
from domain.entities import WorkflowRule, Rule, Workflow, Auditable
from domain.ports import Repository
from infrastructure.data import initial, tables_base


class RepositoryAdapter(Repository):
    """ Repository Adapter """

    def __init__(self, username: str, password: str, server: str, dbname: str):
        self.session: Session = None
        self.engine: Engine = create_engine(
            f"mysql+pymysql://{username}:{
                password}@{server}/{dbname}", echo=True
        )
        event.listen(Workflow, 'before_insert', self.__before_insert)
        event.listen(Rule, 'before_insert', self.__before_insert)
        event.listen(WorkflowRule, 'before_insert', self.__before_insert)

    def rule_read_by_parent_id(self, parent_id: int) -> List[Rule]:
        with Session(self.engine) as session:
            stms = select(Rule).join(WorkflowRule, Rule.id == WorkflowRule.rule_id).where(
                WorkflowRule.workflow_id == parent_id)
            rule = session.scalars(stms).all()
            return rule

    def workflow_read(self, _id: int) -> Workflow:
        with Session(self.engine) as session:
            stmt = select(Workflow).where(Workflow.id == _id)
            workflow = session.scalar(stmt)
            return workflow

    def workflow_read_by_external_id(self, external_id: str) -> Workflow:
        with Session(self.engine) as session:
            stmt = select(Workflow).where(Workflow.name == external_id)
            workflow = session.scalar(stmt)
            return workflow

    def create(self, entity: any):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def begin(self, autoflush=False):
        self.session = Session(self.engine, autoflush=autoflush)

    def commit_work(self):
        if self.session is not None:
            self.session.commit()

    def rollback_work(self):
        if self.session is not None:
            self.session.rollback()

    def migrate(self):
        initial(self.engine)
        tables_base(self.engine)

    def __before_insert(self, mapper, connection, target):
        """ Hook """
        if isinstance(target, Auditable):
            target.created_by = "system"
            target.updated_by = "system"
            target.created_at = datetime.now()
            target.updated_at = datetime.now()

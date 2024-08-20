"""_summary_
    """
from sqlalchemy import select
from sqlalchemy.orm import Session
from domain.entities import Workflow
from domain.ports.entity_repository import WorkflowRepository


class WorkflowAdapter(WorkflowRepository):
    """ Workflow Adapter """

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self, entity: Workflow):
        stmt = select(Workflow).where(Workflow.id == entity.id)
        rule = self.session.scalar(stmt)
        rule.name = entity.name
        rule.expression = entity.expression
        self.session.commit()

    def read(self, _id: int) -> any:
        with Session(self.engine) as session:
            stmt = select(Workflow).where(Workflow.id == _id)
            workflow = session.scalar(stmt)
            return workflow

    def read_by_external_id(self, external_id: str) -> Workflow:
        with Session(self.engine) as session:
            stmt = select(Workflow).where(Workflow.name == external_id)
            workflow = session.scalar(stmt)
            return workflow

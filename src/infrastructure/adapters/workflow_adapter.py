"""_summary_
    """
from sqlalchemy.orm import Session
from domain.entities import Workflow, Pagination
from domain.ports import WorkflowRepository


class WorkflowAdapter(WorkflowRepository):
    """ Workflow Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self, entity: Workflow):
        rule = self.session.query(Workflow).where(
            Workflow.id == entity.id).one_or_none()
        rule.name = entity.name
        rule.expression = entity.expression

    def read(self, _id) -> any:
        with Session(self.engine) as session:
            workflow = session.query(Workflow).where(
                Workflow.id == _id).one_or_none()
            return workflow

    def read_by_external_id(self, external_id) -> Workflow:
        with Session(self.engine) as session:
            workflow = session.query(Workflow).where(
                Workflow.name == external_id).one_or_none()
            return workflow

    def read_page(self, page_no, page_size) -> tuple[list, Workflow]:
        offset = (page_no-1)*page_size
        with Session(self.engine) as session:
            workflows = session.query(Workflow).offset(
                offset).limit(page_size).all()
            total = session.query(Workflow.id).count()

            return workflows, Pagination(page_no, page_size, total)

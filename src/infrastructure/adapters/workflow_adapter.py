"""_summary_
    """
from sqlalchemy import select
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
        stmt = select(Workflow).where(Workflow.id == entity.id)
        rule = self.session.scalar(stmt)
        rule.name = entity.name
        rule.expression = entity.expression

    def read(self, tenantid: int, _id: int) -> any:
        with Session(self.engine) as session:
            stmt = select(Workflow).where(
                Workflow.tenant_id == tenantid,
                Workflow.id == _id)
            workflow = session.scalar(stmt)
            return workflow

    def read_by_external_id(self, tenantid: int, external_id: str) -> Workflow:
        with Session(self.engine) as session:
            stmt = select(Workflow).where(
                Workflow.tenant_id == tenantid,
                Workflow.name == external_id)
            workflow = session.scalar(stmt)
            return workflow

    def read_page(self, tenantid: int, page_no: int, page_size: int) -> tuple[list, Workflow]:
        with Session(self.engine) as session:
            stms = select(Workflow).offset((page_no-1)*page_size).limit(page_size).where(
                Workflow.tenant_id == tenantid)
            rules = session.scalars(stms).all()
            total = session.query(Workflow.id).where(
                Workflow.tenant_id == tenantid).count()

            return rules, Pagination(page_no, page_size, total)

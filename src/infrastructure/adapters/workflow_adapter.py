"""_summary_
    """
from sqlalchemy.orm import Session
from domain.entities import Node, Pagination
from domain.ports import NodeRepository


class WorkflowAdapter(NodeRepository):
    """ Workflow Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self, entity: Node):
        rule = self.session.query(Node).where(
            Node.id == entity.id).one_or_none()
        rule.name = entity.name
        rule.expression = entity.expression

    def read(self, _id) -> any:
        with Session(self.engine) as session:
            workflow = session.query(Node).where(
                Node.id == _id).one_or_none()
            return workflow

    def read_by_external_id(self, external_id) -> Node:
        with Session(self.engine) as session:
            workflow = session.query(Node).where(
                Node.name == external_id).one_or_none()
            return workflow

    def read_page(self, page_no, page_size) -> tuple[list, Node]:
        offset = (page_no-1)*page_size
        with Session(self.engine) as session:
            workflows = session.query(Node).offset(
                offset).limit(page_size).all()
            total = session.query(Node.id).count()

            return workflows, Pagination(page_no, page_size, total)

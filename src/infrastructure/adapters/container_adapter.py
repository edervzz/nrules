"""_summary_
    """
from typing import List
from sqlalchemy.orm import Session
from domain.entities import Container
from domain.ports import ContainerRepository


class ContainerAdapter(ContainerRepository):
    """ Container Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self, entity: Container):
        rule = self.session.query(Container).where(
            Container.tenant_id == entity.tenant_id,
            Container.workflow_id == entity.workflow_id).one_or_none()

        rule.name = entity.name
        rule.expression = entity.expression

    def read_by_parent_id(self, parent_id) -> List[Container]:
        with Session(self.engine) as session:
            containers = session.query(Container).where(
                Container.workflow_id == parent_id).all()
            return containers

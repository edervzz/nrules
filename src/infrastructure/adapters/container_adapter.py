"""_summary_
    """
from typing import List
from sqlalchemy import select
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
        stmt = select(Container).where(
            Container.tenant_id == entity.tenant_id,
            Container.workflow_id == entity.workflow_id)
        rule = self.session.scalar(stmt)
        rule.name = entity.name
        rule.expression = entity.expression

    def read_by_parent_id(self, tenantid: int, parent_id: int) -> List[Container]:
        with Session(self.engine) as session:
            stmt = select(Container).where(
                Container.tenant_id == tenantid,
                Container.workflow_id == parent_id)
            containers = session.scalars(stmt)
            return containers

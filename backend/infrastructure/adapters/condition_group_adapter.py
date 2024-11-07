"""_summary_"""
from typing import List
from sqlalchemy.orm import Session
from domain.entities import ConditionGroup
from domain.ports import ConditionGroupRepository


class ConditionGroupAdapter(ConditionGroupRepository):
    """ Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self,  entity: ConditionGroup):
        expression = self.session.query(ConditionGroup).where(
            ConditionGroup.tenant_id == entity.tenant_id,
            ConditionGroup.id == entity.id).one_or_none()

        expression.expression = entity.expression
        expression.version = entity.version

    def read(self, _id) -> ConditionGroup:
        with Session(self.engine) as session:
            condition = session.query(ConditionGroup).where(
                ConditionGroup.id == _id).one_or_none()
            return condition

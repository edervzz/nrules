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
        pass

    def read(self, _id) -> ConditionGroup:
        with Session(self.engine) as session:
            conditiongroup = session.query(ConditionGroup).where(
                ConditionGroup.id == _id).one_or_none()
            return conditiongroup

    def read_by_parent_id(self, parent_id) -> List[ConditionGroup]:
        with Session(self.engine) as session:
            conditiongroups = session.query(ConditionGroup).where(
                ConditionGroup.rule_id == parent_id).all()
            return conditiongroups

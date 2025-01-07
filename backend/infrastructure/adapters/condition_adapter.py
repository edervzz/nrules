"""_summary_"""
from typing import List
from sqlalchemy.orm import Session
from domain.entities import Condition, ConditionKey
from domain.ports import ConditionRepository


class ConditionAdapter(ConditionRepository):
    """ Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self,  entity: Condition):
        condition = self.session.query(Condition).where(
            Condition.variable == entity.variable,
            Condition.condition_group_id == entity.condition_group_id
        ).one_or_none()

        condition.value = entity.value
        condition.typeof = entity.typeof
        condition.is_case_sensitive = entity.is_case_sensitive

    def read(self, _id: ConditionKey) -> Condition:
        with Session(self.engine) as session:
            condition = session.query(Condition).where(
                Condition.variable == _id.variable,
                Condition.condition_group_id == _id.condition_group_id).one_or_none()
            return condition

    def read_by_parent_id(self, parent_id: str) -> List[Condition]:
        with Session(self.engine) as session:
            conditions = session.query(Condition).where(
                Condition.condition_group_id == parent_id).all()
            return conditions

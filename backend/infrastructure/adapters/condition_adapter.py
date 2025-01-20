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
            Condition.case_id == entity.case_id
        ).one_or_none()

        condition.operator = entity.operator
        condition.value = entity.value

    def read(self, _id: ConditionKey) -> Condition:
        with Session(self.engine) as session:
            condition = session.query(Condition).where(
                Condition.variable == _id.variable,
                Condition.case_id == _id.cas).one_or_none()
            return condition

    def read_by_parent_id(self, parent_id: str) -> List[Condition]:
        with Session(self.engine) as session:
            conditions = session.query(Condition).where(
                Condition.case_id == parent_id).all()
            return conditions

    def read_by_link(self, link_id) -> List[Condition]:
        with Session(self.engine) as session:
            conditions = session.query(Condition).where(
                Condition.rule_id == link_id).all()
            return conditions

    def read_by_link_single(self, link_id, _id):
        with Session(self.engine) as session:
            conditions = session.query(Condition).where(
                Condition.rule_id == link_id,
                Condition.variable == _id).one_or_none()
            return conditions

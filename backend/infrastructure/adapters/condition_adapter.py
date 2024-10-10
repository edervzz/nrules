"""_summary_"""
from typing import List
from sqlalchemy.orm import Session
from domain.entities import Condition
from domain.ports import ConditionRepository


class ConditionAdapter(ConditionRepository):
    """ Condition Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self,  entity: Condition):
        element = self.session.query(Condition).where(
            Condition.tenant_id == entity.tenant_id,
            Condition.rule_id == entity.rule_id,
            Condition.expression_id == entity.expression_id).one_or_none()

        element.position = entity.position
        element.kvs_id_ok = entity.kvs_id_ok
        element.kvs_id_nok = entity.kvs_id_nok
        element.version = entity.version

    def read(self, _id) -> Condition:
        with Session(self.engine) as session:
            condition = session.query(Condition).where(
                Condition.expression_id == _id).one_or_none()
            return condition

    def read_by_parent_id(self, parent_id: int) -> List[Condition]:
        with Session(self.engine) as session:
            matrix = session.query(Condition).where(
                Condition.rule_id == parent_id). order_by(Condition.position).all()
            return matrix

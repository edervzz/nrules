"""_summary_"""
from typing import List
from sqlalchemy.orm import Session
from domain.entities import Condition
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
            Condition.tenant_id == entity.tenant_id,
            Condition.id == entity.id).one_or_none()

        condition.expression = entity.expression
        condition.position = entity.position
        condition.kvs_id_ok = entity.kvs_id_ok
        condition.kvs_id_nok = entity.kvs_id_nok
        condition.version = entity.version

    def read(self, _id) -> Condition:
        with Session(self.engine) as session:
            condition = session.query(Condition).where(
                Condition.id == _id).one_or_none()
            return condition

    def read_by_parent_id(self, parent_id: int) -> List[Condition]:
        with Session(self.engine) as session:
            conditions = session.query(Condition).where(
                Condition.condition_id == parent_id).all()
            return conditions

"""_summary_"""
from typing import List
from sqlalchemy.orm import Session
from domain.entities import Expression
from domain.ports import ExpressionRepository


class ExpressionAdapter(ExpressionRepository):
    """ Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self,  entity: Expression):
        condition = self.session.query(Expression).where(
            Expression.tenant_id == entity.tenant_id,
            Expression.id == entity.id).one_or_none()

        condition.expression = entity.expression
        condition.position = entity.position
        condition.kvs_id_ok = entity.kvs_id_ok
        condition.kvs_id_nok = entity.kvs_id_nok
        condition.version = entity.version

    def read(self, _id) -> Expression:
        with Session(self.engine) as session:
            condition = session.query(Expression).where(
                Expression.id == _id).one_or_none()
            return condition

    def read_by_parent_id(self, parent_id: int) -> List[Expression]:
        with Session(self.engine) as session:
            conditions = session.query(Expression).where(
                Expression.condition_id == parent_id).all()
            return conditions

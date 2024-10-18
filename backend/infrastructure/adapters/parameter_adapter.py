"""_summary_"""
from typing import List
from sqlalchemy.orm import Session
from domain.entities import Parameter
from domain.ports import ParametersRepository


class ParameterAdapter(ParametersRepository):
    """ Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self,  entity: Parameter):
        expression = self.session.query(Parameter).where(
            Parameter.tenant_id == entity.tenant_id,
            Parameter.key == entity.key).one_or_none()

        expression.expression = entity.expression
        expression.version = entity.version

    def read(self, _id) -> Parameter:
        with Session(self.engine) as session:
            condition = session.query(Parameter).where(
                Parameter.key == _id).one_or_none()
            return condition

    def read_by_parent_id(self, parent_id: int) -> List[Parameter]:
        with Session(self.engine) as session:
            conditions = session.query(Parameter).where(
                Parameter.rule_id == parent_id).all()
            return conditions

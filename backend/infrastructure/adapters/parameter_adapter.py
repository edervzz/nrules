"""_summary_"""
from typing import List
from sqlalchemy.orm import Session
from domain.entities import Parameter, ParameterKey
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
        entity.key = entity.key.lower()
        entity.usefor = entity.usefor.upper()
        param = self.session.query(Parameter).where(
            Parameter.key == entity.key,
            Parameter.rule_id == entity.rule_id,
            Parameter.usefor == entity.usefor).one_or_none()

        param.typeof = entity.typeof
        param.is_active = entity.is_active
        param.is_archived = entity.is_archived

    def read(self, _id: ParameterKey) -> Parameter:
        _id.key = _id.key.lower()
        _id.usefor = _id.usefor.upper()
        with Session(self.engine) as session:
            parameters = session.query(Parameter).where(
                Parameter.rule_id == _id.rule_id,
                Parameter.key == _id.key,
                Parameter.usefor == _id.usefor).one_or_none()
            return parameters

    def read_by_parent_id(self, parent_id: int) -> List[Parameter]:
        with Session(self.engine) as session:
            parameters = session.query(Parameter).where(
                Parameter.rule_id == parent_id).all()
            return parameters

"""_summary_
    """
from sqlalchemy.orm import Session
from domain.entities import Condition
from domain.ports import ConditionRepository


class ConditionAdapter(ConditionRepository):
    """ Rule Adapter """

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
        condition.operator = entity.operator
        condition.version = entity.version

    def read(self, _id) -> Condition:
        with Session(self.engine) as session:
            rule = session.query(Condition).where(
                Condition.id == _id).one_or_none()
            return rule

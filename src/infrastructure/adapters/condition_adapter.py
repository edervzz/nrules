"""_summary_
    """
from sqlalchemy.orm import Session
from domain.entities import Conditions
from domain.ports import CaseRepository


class ConditionAdapter(CaseRepository):
    """ Rule Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self,  entity: Conditions):
        condition = self.session.query(Conditions).where(
            Conditions.tenant_id == entity.tenant_id,
            Conditions.id == entity.id).one_or_none()

        condition.expression = entity.expression
        condition.position = entity.position
        condition.kvs_id = entity.kvs_id
        condition.kvs_id_nok = entity.kvs_id_nok
        condition.version = entity.version

    def read(self, _id) -> Conditions:
        with Session(self.engine) as session:
            rule = session.query(Conditions).where(
                Conditions.id == _id).one_or_none()
            return rule

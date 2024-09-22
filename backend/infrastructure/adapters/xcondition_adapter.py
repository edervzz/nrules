"""_summary_
    """
from sqlalchemy.orm import Session
from domain.entities import XCondition
from domain.ports import XConditionRepository


class XConditionAdapter(XConditionRepository):
    """ X- Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity: XCondition):
        new_entity = XCondition()
        new_entity.id = entity.id

        with Session(self.engine) as session:
            session.add(new_entity)
            session.flush()
            entity.id = new_entity.id
            session.commit()

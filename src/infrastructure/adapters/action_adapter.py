"""_summary_
    """
from sqlalchemy import select
from sqlalchemy.orm import Session
from domain.entities import Action
from domain.ports import ActionRepository


class ActionAdapter(ActionRepository):
    """ Action Adapter """
    
    def set_session(self, session: Session):
        self.session = session
        
    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def read(self, tenantid: int, _id: int) -> Action:
        with Session(self.engine) as session:
            stmt = select(Action).where(
                Action.tenant_id == tenantid,
                Action.id == _id)
            rule = session.scalar(stmt)
            return rule

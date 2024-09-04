"""_summary_
    """
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

    def read(self, _id) -> Action:
        with Session(self.engine) as session:
            rule = session.query(Action).where(Action.id == _id).one_or_none()
            return rule

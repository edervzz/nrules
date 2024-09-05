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

    def update(self, entity: Action):
        action = self.session.query(Action).where(
            Action.id == entity.id).one_or_none()

        action.name = entity.name
        action.ruleset_id = entity.ruleset_id
        action.kv_id = entity.kv_id
        action.version = entity.version

    def read(self, _id) -> Action:
        with Session(self.engine) as session:
            rule = session.query(Action).where(Action.id == _id).one_or_none()
            return rule

    def read_by_external_id(self, external_id: str) -> any:
        with Session(self.engine) as session:
            rule = session.query(Action).where(
                Action.name == external_id).one_or_none()
            return rule

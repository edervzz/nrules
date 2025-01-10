"""_summary_
    """
from sqlalchemy.orm import Session
from domain.entities import XObject


class XObjectAdapter():
    """ X-Object Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity: XObject):
        new_entity = XObject()
        new_entity.id = entity.id
        new_entity.object_name = entity.object_name

        with Session(self.engine) as session:
            entity.object_name = entity.object_name.upper()
            session.add(new_entity)
            session.flush()
            entity.id = new_entity.id
            session.commit()

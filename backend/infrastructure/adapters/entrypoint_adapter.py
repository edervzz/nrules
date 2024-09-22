"""_summary_
    """

from sqlalchemy.orm import Session
from domain.entities import Entrypoint
from domain.ports import EntrypointRepository


class EntrypointAdapter(EntrypointRepository):
    """ entrypoint Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def read(self, _id) -> any:
        with Session(self.engine) as session:
            container = session.query(Entrypoint).where(
                Entrypoint.id == _id).one_or_none()
            return container

    def read_by_external_id(self, external_id) -> Entrypoint:
        with Session(self.engine) as session:
            container = session.query(Entrypoint).where(
                Entrypoint.name == external_id).one_or_none()
            return container

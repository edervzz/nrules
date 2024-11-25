"""_summary_
    """
from sqlalchemy.orm import Session
from domain.entities import KVStorage
from domain.ports import KVStorageRepository


class KVStorageAdapter(KVStorageRepository):
    """ KV Storage Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def read(self, _id) -> KVStorage:
        with Session(self.engine) as session:
            rule = session.query(KVStorage).where(
                KVStorage.id == _id).one_or_none()
            return rule

    def read_by_external_id(self, external_id) -> any:
        with Session(self.engine) as session:
            rule = session.query(KVStorage).where(
                KVStorage.name == external_id).one_or_none()
            return rule

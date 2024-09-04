"""_summary_
    """
from sqlalchemy.orm import Session
from domain.entities import KV
from domain.ports import KVSRepository


class KVSAdapter(KVSRepository):
    """ KVS Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def read(self, _id) -> KV:
        with Session(self.engine) as session:
            rule = session.query(KV).where(KV.id == _id).one_or_none()
            return rule

    def read_by_external_id(self, external_id) -> any:
        with Session(self.engine) as session:
            rule = session.query(KV).where(
                KV.name == external_id).one_or_none()
            return rule

"""_summary_
    """
from typing import List
from sqlalchemy.orm import Session
from domain.entities import KV
from domain.ports import KVSRepository


class KVSAdapter(KVSRepository):
    """ KV Storage Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def read(self, _id) -> KV:
        with Session(self.engine) as session:
            rule = session.query(KV).where(
                KV.id == _id).one_or_none()
            return rule

    def read_by_parent_id(self, parent_id) -> List[KV]:
        with Session(self.engine) as session:
            rules = session.query(KV).where(KV.rule_id == parent_id).all()
            return rules

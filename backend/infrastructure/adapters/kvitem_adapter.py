"""_summary_
    """
from typing import List
from sqlalchemy.orm import Session
from domain.entities import KVItem, KVItemKey
from domain.ports import KVItemRepository


class KVItemAdapter(KVItemRepository):
    """ KV Item Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self, entity: KVItem):
        kvitem = self.session.query(KVItem).where(
            KVItem.kv_id == entity.kv_id,
            KVItem.key == entity.key).one_or_none()

        kvitem.value = entity.value
        kvitem.typeof = entity.typeof

    def read(self, _id: KVItemKey) -> KVItem:
        with Session(self.engine) as session:
            rule = session.query(KVItem).where(
                KVItem.kv_id == _id.kv_id,
                KVItem.key == _id.key).one_or_none()
            return rule

    def read_by_parent_id(self, parent_id: str) -> List[KVItem]:
        with Session(self.engine) as session:
            kvitems = session.query(KVItem).where(
                KVItem.kv_id == parent_id).all()
            return kvitems

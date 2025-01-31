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
        entity.key = entity.key.upper()
        kvitem = self.session.query(KVItem).where(
            KVItem.case_id == entity.case_id,
            KVItem.key == entity.key).one_or_none()

        kvitem.value = entity.value
        kvitem.calculation = entity.calculation

    def read(self, _id: KVItemKey) -> KVItem:
        _id.key = _id.key.upper()
        with Session(self.engine) as session:
            rule = session.query(KVItem).where(
                KVItem.case_id == _id.case_id,
                KVItem.key == _id.key).one_or_none()
            return rule

    def read_by_parent_id(self, parent_id: str) -> List[KVItem]:
        with Session(self.engine) as session:
            kvitems = session.query(KVItem).where(
                KVItem.case_id == parent_id).all()
            return kvitems

    def read_by_link(self, link_id) -> List[KVItem]:
        with Session(self.engine) as session:
            conditions = session.query(KVItem).where(
                KVItem.rule_id == link_id).all()
            return conditions

    def read_by_link_single(self, link_id, _id: str):
        _id = _id.upper()
        with Session(self.engine) as session:
            conditions = session.query(KVItem).where(
                KVItem.rule_id == link_id,
                KVItem.key == _id).one_or_none()
            return conditions

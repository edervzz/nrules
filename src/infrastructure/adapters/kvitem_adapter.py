"""_summary_
    """
from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from domain.entities import KVItem
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
        stmt = select(KVItem).where(
            KVItem.tenant_id == entity.tenant_id,
            KVItem.key == entity.key)
        kvitem = self.session.scalar(stmt)
        kvitem.value = entity.value
        kvitem.typeof = entity.typeof
        kvitem.version = entity.version

    def read_by_external_id(self, tenantid: int, external_id: str) -> KVItem:
        with Session(self.engine) as session:
            stmt = select(KVItem).where(
                KVItem.tenant_id == tenantid,
                KVItem.key == external_id)
            rule = session.scalar(stmt)
            return rule

    def read_by_parent_id(self, tenantid: int, parent_id: int) -> List[KVItem]:
        with Session(self.engine) as session:
            stms = select(KVItem).where(
                KVItem.tenant_id == tenantid,
                KVItem.kv_id == parent_id)
            kvitems = session.scalars(stms).all()
            return kvitems

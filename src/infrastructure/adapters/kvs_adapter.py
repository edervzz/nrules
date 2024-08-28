"""_summary_
    """
from sqlalchemy import select
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

    def read(self, tenantid: int, _id: int) -> KV:
        with Session(self.engine) as session:
            stmt = select(KV).where(
                KV.tenant_id == tenantid,
                KV.id == _id)
            rule = session.scalar(stmt)
            return rule

    def read_by_external_id(self, tenantid: int, external_id: str) -> any:
        with Session(self.engine) as session:
            stmt = select(KV).where(
                KV.tenant_id == tenantid,
                KV.name == external_id)
            rule = session.scalar(stmt)
            return rule

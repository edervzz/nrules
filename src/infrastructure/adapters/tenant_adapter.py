"""_summary_
    """
from sqlalchemy import select
from sqlalchemy.orm import Session
from domain.entities import Tenants
from domain.ports import TenantRepository


class TenantAdapter(TenantRepository):
    """ Rule Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def read(self, tenantid: int,  _id: int) -> Tenants:
        with Session(self.engine) as session:
            stmt = select(Tenants).where(Tenants.id == 3000 + _id)
            rule = session.scalar(stmt)
            return rule

    def read_by_external_id(self, tenantid: int, external_id: str) -> Tenants:
        with Session(self.engine) as session:
            stmt = select(Tenants).where(Tenants.name == external_id)
            rule = session.scalar(stmt)
            return rule

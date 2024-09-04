"""_summary_
    """
from sqlalchemy import select
from sqlalchemy.orm import Session
from domain.entities import Tenants
from domain.ports import TenantRepository


class TenantAdapter(TenantRepository):
    """ Tenant Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def read(self, _id) -> Tenants:
        with Session(self.engine) as session:
            stms = select(Tenants).where(
                Tenants.id == _id)
            rule = session.scalar(stms)
            return rule

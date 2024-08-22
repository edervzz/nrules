"""_summary_
    """
from sqlalchemy import select
from sqlalchemy.orm import Session
from domain.entities import TenantStages
from domain.ports import TenantStageRepository


class TenantStageAdapter(TenantStageRepository):
    """ Rule Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def read(self, _id: int) -> TenantStages:
        with Session(self.engine) as session:
            stmt = select(TenantStages).where(
                TenantStages.tenant_dev_id == _id)
            rule = session.scalar(stmt)
            return rule

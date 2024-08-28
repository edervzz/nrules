"""_summary_
    """
from sqlalchemy import select
from sqlalchemy.orm import Session
from domain.entities import Tenants
from domain.entities.tenant_stages import TenantStages
from domain.ports import TenantStageRepository


class TenantStageAdapter(TenantStageRepository):
    """ Tenant Stage Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self, entity: TenantStages):
        stmt = select(TenantStages).where(
            TenantStages.tenant_dev_id == entity.tenant_dev_id)
        stage = self.session.scalar(stmt)
        stage.tenant_test_id = entity.tenant_test_id
        stage.tenant_release_id = entity.tenant_release_id

    def read(self, tenantid: int, _id: int) -> TenantStages:
        with Session(self.engine) as session:
            stmt = select(TenantStages).where(
                TenantStages.tenant_dev_id == _id)
            rule = session.scalar(stmt)
            return rule

    def read_by_external_id(self, tenantid: int, external_id: str) -> TenantStages:
        with Session(self.engine) as session:
            stmt = select(Tenants).where(Tenants.name == external_id)
            tenant = session.scalar(stmt)

            stmt = select(TenantStages).where(
                TenantStages.tenant_dev_id == tenant.id)
            tenant_stage = session.scalar(stmt)

            return tenant_stage

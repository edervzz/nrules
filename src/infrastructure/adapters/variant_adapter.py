"""_summary_"""
from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from domain.entities import Variant
from domain.ports import VariantRepository


class VariantAdapter(VariantRepository):
    """ Variant Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self,  entity: Variant):
        stmt = select(Variant).where(
            Variant.tenant_id == entity.tenant_id,
            Variant.key == entity.key)
        rule = self.session.scalar(stmt)
        rule.value = entity.value
        rule.version = entity.version

    def read_by_parent_id(self, tenantid: int, parent_id: int) -> List[Variant]:
        with Session(self.engine) as session:
            stmt = select(Variant).where(
                Variant.tenant_id == tenantid,
                Variant.entrypoint_key == parent_id)
            containers = session.scalars(stmt)
            return containers

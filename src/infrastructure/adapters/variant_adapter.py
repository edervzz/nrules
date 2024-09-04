"""_summary_"""
from typing import List
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
        rule = self.session.query(Variant).where(
            Variant.key == entity.key).one_or_none()

        rule.value = entity.value
        rule.version = entity.version

    def read_by_parent_id(self, parent_id) -> List[Variant]:
        with Session(self.engine) as session:
            variants = session.query(Variant).where(
                Variant.entrypoint_key == parent_id).all()
            return variants

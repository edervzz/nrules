"""_summary_"""
from typing import List
from sqlalchemy.orm import Session
from domain.entities import Case
from domain.ports import CaseRepository


class CaseAdapter(CaseRepository):
    """ Condition Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self,  entity: Case):
        element = self.session.query(Case).where(
            Case.tenant_id == entity.tenant_id,
            Case.rule_id == entity.rule_id,
            Case.id == entity.expression_id).one_or_none()

        element.position = entity.position
        element.is_active = entity.is_active
        element.is_archived = entity.is_archived

    def read(self, _id) -> Case:
        with Session(self.engine) as session:
            condition = session.query(Case).where(
                Case.id == _id).one_or_none()
            return condition

    def read_by_parent_id(self, parent_id: int) -> List[Case]:
        with Session(self.engine) as session:
            matrix = session.query(Case).where(
                Case.rule_id == parent_id). order_by(Case.position).all()
            return matrix

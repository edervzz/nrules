"""_summary_
    """
from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from domain.entities import Rule, Container, Pagination
from domain.ports import RuleRepository


class RuleAdapter(RuleRepository):
    """ Rule Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self,  entity: Rule):
        stmt = select(Rule).where(
            Rule.tenant_id == entity.tenant_id,
            Rule.id == entity.id)
        rule = self.session.scalar(stmt)
        rule.name = entity.name
        rule.expression = entity.expression
        rule.version = entity.version

    def read(self, tenantid: int, _id: int) -> Rule:
        with Session(self.engine) as session:
            stmt = select(Rule).where(
                Rule.tenant_id == tenantid, Rule.id == _id)
            rule = session.scalar(stmt)
            return rule

    def read_by_external_id(self, tenantid: int, external_id: str) -> Rule:
        with Session(self.engine) as session:
            stmt = select(Rule).where(
                Rule.tenant_id == tenantid,
                Rule.name == external_id)
            rule = session.scalar(stmt)
            return rule

    def read_by_parent_id(self, tenantid: int, parent_id: int) -> List[Rule]:
        with Session(self.engine) as session:
            stms = select(Rule).join(Container, Rule.id == Container.rule_id).where(
                Container.tenant_id == tenantid,
                Container.workflow_id == parent_id)
            rule = session.scalars(stms).all()
            return rule

    def read_page(self, tenantid: int, page_no: int, page_size: int) -> tuple[List[Rule], Pagination]:
        with Session(self.engine) as session:
            stms = select(Rule).offset((page_no-1)*page_size).limit(page_size).where(
                Rule.tenant_id == tenantid)
            rules = session.scalars(stms).all()
            total = session.query(Rule.id).where(
                Rule.tenant_id == tenantid).count()

            return rules, Pagination(page_no, page_size, total)

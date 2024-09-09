"""_summary_
    """
from typing import List
from sqlalchemy.orm import Session
from domain.entities import Rule, Pagination
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
        rule = self.session.query(Rule).where(
            Rule.tenant_id == entity.tenant_id,
            Rule.id == entity.id).one_or_none(9)

        rule.name = entity.name
        rule.expression = entity.expression
        rule.version = entity.version

    def read(self, _id) -> Rule:
        with Session(self.engine) as session:
            rule = session.query(Rule).where(Rule.id == _id).one_or_none()
            return rule

    def read_by_external_id(self, external_id) -> Rule:
        with Session(self.engine) as session:
            rule = session.query(Rule).where(
                Rule.name == external_id).one_or_none()
            return rule

    def read_page(self, page_no, page_size) -> tuple[List[Rule], Pagination]:
        with Session(self.engine) as session:
            offset = (page_no-1)*page_size
            rules = session.query(Rule).offset(offset).limit(page_size).all()
            total = session.query(Rule.id).where().count()

            return rules, Pagination(page_no, page_size, total)

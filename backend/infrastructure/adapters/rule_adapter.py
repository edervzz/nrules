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

    def update(self, entity: Rule):
        rule: Rule
        rule = self.session.query(Rule).where(
            Rule.id == entity.id).one_or_none()

        rule.strategy = entity.strategy

    def read(self, _id) -> Rule:
        with Session(self.engine) as session:
            rule = session.query(Rule).where(Rule.id == _id).one_or_none()
            return rule

    def read_by_external_id(self, external_id) -> Rule:
        with Session(self.engine) as session:
            rule = session.query(Rule).where(
                Rule.name == external_id).one_or_none()
            return rule

    def read_page(self, page_no, page_size, word) -> tuple[List[Rule], Pagination]:
        with Session(self.engine) as session:
            offset = (page_no-1)*page_size
            if word != "":
                rules = session.query(
                    Rule).where(Rule.name.ilike(f'%{word}%')).order_by(Rule.name).offset(offset).limit(page_size).all()
            else:
                rules = session.query(Rule).order_by(Rule.name).offset(
                    offset).limit(page_size).all()
            total = session.query(
                Rule.id).where(Rule.name.ilike(f'%{word}%')).all()
            return rules, Pagination(page_no, page_size, len(total))

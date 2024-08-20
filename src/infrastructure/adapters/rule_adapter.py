"""_summary_
    """
from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from domain.entities import Rule, WorkflowRule
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
        stmt = select(Rule).where(Rule.id == entity.id)
        rule = self.session.scalar(stmt)
        rule.name = entity.name
        rule.expression = entity.expression
        self.session.commit()

    def read(self, _id: int) -> Rule:
        with Session(self.engine) as session:
            stmt = select(Rule).where(Rule.id == _id)
            rule = session.scalar(stmt)
            return rule

    def read_by_external_id(self, external_id: str) -> Rule:
        with Session(self.engine) as session:
            stmt = select(Rule).where(Rule.name == external_id)
            rule = session.scalar(stmt)
            return rule

    def read_by_parent_id(self, parent_id: int) -> List[Rule]:
        with Session(self.engine) as session:
            stms = select(Rule).join(WorkflowRule, Rule.id == WorkflowRule.rule_id).where(
                WorkflowRule.workflow_id == parent_id)
            rule = session.scalars(stms).all()
            return rule

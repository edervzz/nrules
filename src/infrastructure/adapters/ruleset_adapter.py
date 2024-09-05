"""_summary_
    """
from sqlalchemy.orm import Session
from domain.entities import Ruleset, Pagination
from domain.ports import RulesetRepository


class RulesetAdapter(RulesetRepository):
    """ Workflow Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self, entity: Ruleset):
        rule = self.session.query(Ruleset).where(
            Ruleset.id == entity.id).one_or_none()
        rule.name = entity.name
        rule.expression = entity.expression

    def read(self, _id) -> any:
        with Session(self.engine) as session:
            workflow = session.query(Ruleset).where(
                Ruleset.id == _id).one_or_none()
            return workflow

    def read_by_external_id(self, external_id) -> Ruleset:
        with Session(self.engine) as session:
            workflow = session.query(Ruleset).where(
                Ruleset.name == external_id).one_or_none()
            return workflow

    def read_page(self, page_no, page_size) -> tuple[list, Ruleset]:
        offset = (page_no-1)*page_size
        with Session(self.engine) as session:
            workflows = session.query(Ruleset).offset(
                offset).limit(page_size).all()
            total = session.query(Ruleset.id).count()

            return workflows, Pagination(page_no, page_size, total)

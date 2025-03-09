"""_summary_
    """
from typing import List
from sqlalchemy.orm import Session
from domain.entities import Tag
from domain.ports import TagRepository


class TagAdapter(TagRepository):
    """ Rule Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self, entity: Tag):
        tag: Tag
        tag = self.session.query(Tag).where(
            Tag.key == entity.key).one_or_none()

        tag.value = entity.value

    def read_by_external_id(self, external_id) -> Tag:
        external_id = external_id.lower()
        with Session(self.engine) as session:
            tag = session.query(Tag).where(
                Tag.value == external_id).one_or_none()
            return tag

    def read_by_parent_id(self, parent_id) -> List[Tag]:
        with Session(self.engine) as session:
            tags = session.query(Tag).where(
                Tag.rule_id == parent_id).all()
            return tags

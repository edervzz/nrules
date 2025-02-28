"""_summary_"""
from typing import List
from sqlalchemy.orm import Session
from domain.entities import Node
from domain.ports import NodeRepository


class NodeAdapter(NodeRepository):
    """ Condition Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self,  entity: Node):
        element = self.session.query(Node).where(
            Node.rule_id == entity.rule_id,
            Node.id == entity.id).one_or_none()

        element.right_node_id = entity.right_node_id
        element.left_node_id = entity.left_node_id
        element.is_active = entity.is_active
        element.is_archived = entity.is_archived

    def read(self, _id) -> Node:
        with Session(self.engine) as session:
            if len(_id) == 8:
                condition = session.query(Node).where(
                    Node.id.ilike(f'{_id}%')).one_or_none()
            else:
                condition = session.query(Node).where(
                    Node.id == _id).one_or_none()
            return condition

    def read_by_parent_id(self, parent_id: int) -> List[Node]:
        with Session(self.engine) as session:
            matrix = session.query(Node).where(
                Node.rule_id == parent_id).all()
            return matrix

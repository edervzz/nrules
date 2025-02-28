"""_summary_"""
from typing import List
from domain.entities import Node, Condition, KVItem, Rule, Case


class CreateNodeRuleRequest:
    """ create a new node """

    def __init__(
            self,
            _id: str,
            name: str,
            parent_node_id: str,
            assign_node_to: str,  # LEFT / RIGHT
    ):
        self.id = _id
        self.name = name
        self.parent_node_id = parent_node_id,
        self.assign_node_to = assign_node_to

        self.new_node: Node = None
        self.case: Case = None
        self.conditions: List[Condition] = []
        self.kvitems: List[KVItem] = []

        self.rule: Rule
        self.parent_node: Node


class CreateNodeRuleResponse:
    """ create a new node response """

    def __init__(self, _id: str):
        self.id = _id

""" create rule messages """
from typing import List
from domain.entities import Rule, Parameter, Case, KVItem, Condition, Tag, Node


class CreateRuleRequest:
    """ Create Rule Request """

    def __init__(
            self,
            rule: Rule,
            parameters: List[Parameter],
            tags: List[Tag]
    ):
        self.parameters = parameters

        self.tags = tags

        self.tags = tags

        self.rule = rule

        self.case_zero = Case()

        self.conditions: List[Condition] = []

        self.kv_items: List[KVItem] = []

        self.node: Node = None


class CreateRuleResponse:
    """ Create Rule Response """

    def __init__(self, _id):
        self.id = _id

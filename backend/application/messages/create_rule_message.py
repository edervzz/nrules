""" create rule messages """
from typing import List
from domain.entities import Rule, KV, Parameter, Case, KVItem, ConditionGroup, Condition, Tag


class CreateRuleRequest:
    """ Create Rule Request """

    def __init__(
            self,
            rule: Rule,
            use_default: bool,
            parameters: List[Parameter],
            tags: List[Tag]
    ):
        self.parameters = parameters

        self.tags = tags

        self.tags = tags

        self.default_kvs = KV()

        self.rule = rule

        self.use_default = use_default

        self.condition_group = ConditionGroup()

        self.kvs = KV()

        self.default_case = Case()

        self.conditions: List[Condition] = []

        self.kv_items: List[KVItem] = []


class CreateRuleResponse:
    """ Create Rule Response """

    def __init__(self, _id):
        self.id = _id

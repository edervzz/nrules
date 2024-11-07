""" create rule messages """
from typing import List
from domain.entities import Rule, KV, Parameter, Case, KVItem, ConditionGroup, Condition


class CreateRuleRequest:
    """ Create Rule Request """

    def __init__(
            self,
            rule: Rule,
            parameters: List[Parameter]
    ):
        self.parameters = parameters

        self.default_kvs = KV()

        self.rule = rule

        self.condition_group = ConditionGroup()

        self.kvs = KV()

        self.case = Case()

        self.conditions: List[Condition] = []

        self.kv_items: List[KVItem] = []


class CreateRuleResponse:
    """ Create Rule Response """

    def __init__(self, _id):
        self.id = _id

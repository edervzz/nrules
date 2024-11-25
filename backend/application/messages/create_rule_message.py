""" create rule messages """
from typing import List
from domain.entities import Rule, KVStorage, Parameter, Case, KVItem, ConditionGroup, Condition


class CreateRuleRequest:
    """ Create Rule Request """

    def __init__(
            self,
            rule: Rule,
            use_default: bool,
            parameters: List[Parameter]
    ):
        self.parameters = parameters

        self.default_kvs = KVStorage()

        self.rule = rule

        self.use_default = use_default

        self.condition_group = ConditionGroup()

        self.kvs = KVStorage()

        self.case = Case()

        self.case_default = Case()

        self.conditions: List[Condition] = []

        self.kv_items: List[KVItem] = []


class CreateRuleResponse:
    """ Create Rule Response """

    def __init__(self, _id):
        self.id = _id

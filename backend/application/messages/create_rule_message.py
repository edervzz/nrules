""" create rule messages """
from typing import List
from domain.entities import Case, Condition, Rule, KVItem, KV, Parameter


class CreateRuleRequest:
    """ Create Rule Request """

    def __init__(
            self,
            ruleid: str,
            name: str,
            rule_type: str,
            strategy: str,
            parameters: List[Parameter],
            # kvs: List[KV],
            # kvitems: List[KVItem],
            # conditions: List[Condition],
            # expressions: List[Expression],
            # default_kvs: KV,
            # default_kvitems: List[KVItem]
    ):

        self.rule = Rule()
        self.rule.id = ruleid
        self.rule.name = name
        self.rule.rule_type = rule_type
        self.rule.strategy = strategy
        self.paramters = parameters

        # self.conditions = conditions
        # self.expressions = expressions
        # self.kvs = kvs
        # self.kvitems = kvitems

        # self.default_kvs = default_kvs
        # self.default_kvitems = default_kvitems


class CreateRuleResponse:
    """ Create Rule Response """

    def __init__(self, _id):
        self.id = _id

""" create rule messages """
from typing import List
from domain.entities import Condition, Expression, Rule, KVItem, KV


class CreateRuleRequest:
    """ Create Rule Request """

    def __init__(
            self,
            name: str,
            rule_type: str,
            strategy: str,
            kvs: List[KV],
            kvitems: List[KVItem],
            conditions: List[Condition],
            expressions: List[Expression]):

        self.rule = Rule()
        self.rule.name = name
        self.rule.rule_type = rule_type
        self.rule.strategy = strategy

        self.conditions = conditions
        self.expressions = expressions
        self.kvs = kvs
        self.kvitems = kvitems


class CreateRuleResponse:
    """ Create Rule Response """

    def __init__(self, _id):
        self.id = _id

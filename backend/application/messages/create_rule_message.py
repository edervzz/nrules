""" create rule messages """
from typing import List
from domain.entities import Case, Condition, Rule


class CreateRuleRequest:
    """ Create Rule Request """

    def __init__(self, name: str, rule_type: str, strategy: str, kvs_id_nok: int, matrix: List[Case], conditions: List[Condition]):
        self.rule = Rule()
        self.rule.name = name
        self.rule.rule_type = rule_type
        self.rule.strategy = strategy
        self.rule.kvs_id_nok = kvs_id_nok

        self.matrix = matrix
        self.conditions = conditions


class CreateRuleResponse:
    """ Create Rule Response """

    def __init__(self, _id):
        self.id = _id

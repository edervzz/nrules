""" create rule messages """
from typing import List
from domain.entities import Condition, Rule


class CreateRuleRequest:
    """ Create Rule Request """

    def __init__(self, name: str, rule_type: str, kvs_id_nok: int, conditions: List[Condition]):
        self.rule = Rule()
        self.rule.name = name
        self.rule.rule_type = rule_type
        self.rule.kvs_id_nok = kvs_id_nok

        self.conditions = conditions


class CreateRuleResponse:
    """ Create Rule Response """

    def __init__(self, _id):
        self.id = _id

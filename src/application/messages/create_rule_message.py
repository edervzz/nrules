""" create rule messages """
from typing import List
from domain.entities import Conditions, Rule


class CreateRuleRequest:
    """ Create Rule Request """

    def __init__(self, name: str, rule_type: str, result_default: str, kvsid: int, cases: List[Conditions]):
        self.rule = Rule()
        self.rule.name = name
        self.rule.rule_type = rule_type
        self.rule.result_default = result_default
        self.rule.kvs_id_nok = kvsid

        self.cases = cases


class CreateRuleResponse:
    """ Create Rule Response """

    def __init__(self, _id):
        self.id = _id

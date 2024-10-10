""" create rule messages """
from typing import List
from domain.entities import Rule
from domain.entities import Condition


class UpdateRuleRequest:
    """ Update Rule Request """

    def __init__(self, _id: int, name: str, kvs_id_nok: int, conditions: List[Condition]):
        self.rule = Rule()
        self.rule.id = _id
        self.rule.name = name
        self.rule.kvs_id_nok = kvs_id_nok

        self.conditions = conditions


class UpdateRuleResponse:
    """ Update Rule Response """

    def __init__(self, _id):
        self.id = _id

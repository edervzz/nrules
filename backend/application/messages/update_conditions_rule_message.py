""" Save conditions rules """
from typing import List
from domain.entities import Condition, Rule


class UpdateConditionsRuleRequest:
    """ Update Conditions Rule """

    def __init__(
            self,
            _id: str,
            name: str,
            conditions: List[Condition]):

        self.id = _id
        self.name = name
        self.income_conditions: List[Condition] = conditions

        self.rule: Rule


class UpdateConditionsRuleResponse:
    """ Update Conditions Rule Response """

    def __init__(self, _id):
        self.id = _id

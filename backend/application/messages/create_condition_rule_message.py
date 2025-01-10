""" Save conditions rules """
from typing import List
from domain.entities import Parameter, Condition


class CreateConditionsRuleRequest:
    """ Create Conditions Rule """

    def __init__(
            self,
            _id: str,
            name: str,
            conditions: List[Condition]):

        self.id = _id
        self.name = name
        self.income_conditions: List[Condition] = conditions
        self.new_parameters: List[Parameter] = []
        self.new_conditions: List[Condition] = []


class CreateConditionsRuleResponse:
    """ Create Conditions Rule Response """

    def __init__(self, _id):
        self.id = _id

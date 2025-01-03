""" Save conditions rules """
from typing import List
from domain.entities import Parameter, Condition


class SaveConditionsRuleRequest:
    """ Save Conditions Rule """

    def __init__(
            self,
            _id: int,
            name: str,
            insert_cond_parameters: List[Condition],
            update_cond_parameters: List[Condition]):
        self.id = _id
        self.name = name
        self.insert_cond_parameters: List[Condition] = insert_cond_parameters
        self.update_cond_parameters: List[Condition] = update_cond_parameters

        self.insert_parameters: List[Parameter] = []
        self.update_parameters: List[Parameter] = []


class SaveConditionsRuleResponse:
    """ Save Conditions Rule Response """

    def __init__(self, _id):
        self.id = _id

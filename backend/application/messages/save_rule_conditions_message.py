""" Save conditions rules """
from typing import List
from domain.entities import Condition, Parameter


class SaveRuleConditionsRequest:
    """ Save Conditions Rules """

    def __init__(self, _id: int, name: str, upsert_conditions: List[Condition], delete_conditions: List[Condition]):
        self.id = _id
        self.name = name
        self.upsert_conditions = upsert_conditions
        self.delete_conditions = delete_conditions

        self.insert_conditions: List[Condition] = []
        self.update_conditions: List[Condition] = []

        self.insert_parameters: List[Parameter] = []
        self.update_parameter: List[Parameter] = []


class SaveRuleConditionsResponse:
    """ Save Conditions Rules Response """

    def __init__(self, _id):
        self.id = _id

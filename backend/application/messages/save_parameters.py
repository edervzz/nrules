""" create rule messages """
from typing import List
from domain.entities import Rule, Parameter, Condition


class SaveConditionParamsRequest:
    """ Save Parameters Request """

    def __init__(
            self,
            _id: int,
            name: str,
            param_cond_upsert: List[Parameter]):
        self.rule = Rule()
        self.rule.id = _id
        self.rule.name = name
        self.param_cond_upsert = param_cond_upsert

        self.param_cond_to_insert: List[Parameter] = []
        self.param_cond_to_update: List[Parameter] = []

        self.conditions_to_insert: List[Condition] = []
        self.conditions_to_update: List[Condition] = []


class SaveConditionParamsResponse:
    """ Save Parameters Response """

    def __init__(self, _id):
        self.id = _id

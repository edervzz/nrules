""" create rule messages """
from typing import List
from domain.entities import Rule, Parameter, Condition, KVItem


class UpdateRuleParamsRequest:
    """ Save Parameters Request """

    def __init__(
            self,
            _id: int,
            name: str,
            params_upsert: List[Parameter]):
        self.rule = Rule()
        self.rule.id = _id
        self.rule.name = name
        self.params_upsert = params_upsert

        self.parameters_to_insert: List[Parameter] = []
        self.parameters_to_update: List[Parameter] = []

        self.conditions_to_insert: List[Condition] = []
        self.conditions_to_update: List[Condition] = []

        self.output_to_insert: List[KVItem] = []
        self.output_to_update: List[KVItem] = []


class UpdateRuleParamsResponse:
    """ Save Parameters Response """

    def __init__(self, _id):
        self.id = _id

""" Save conditions rules """
from typing import List
from domain.entities import Parameter, Condition, KVItem, Rule


class CreateParamtersRuleRequest:
    """ Create Paramters Rule """

    def __init__(
            self,
            _id: str,
            name: str,
            parameters: List[Parameter]):

        self.id = _id
        self.name = name
        self.parameters: List[Parameter] = parameters

        self.income_conditions: List[Condition] = []
        self.conditions: List[Condition] = []

        self.income_kvitems: List[KVItem] = []
        self.kvitems: List[KVItem] = []

        self.rule: Rule


class CreateParametersRuleResponse:
    """ Create Parameters Rule Response """

    def __init__(self, _id):
        self.id = _id

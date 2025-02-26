""" Save conditions rules """
from typing import List
from domain.entities import Parameter, Rule


class UpdateParametersRuleRequest:
    """ Update Parameters Rule """

    def __init__(
            self,
            _id: str,
            name: str,
            parameters: List[Parameter]):

        self.id = _id
        self.name = name
        self.parameters: List[Parameter] = parameters

        self.rule: Rule


class UpdateParametersRuleResponse:
    """ Update Parameters Rule Response """

    def __init__(self, _id):
        self.id = _id

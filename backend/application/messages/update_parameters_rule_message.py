""" Save conditions rules """
from typing import List
from domain.entities import Parameter, Condition, KVItem


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


class UpdateParametersRuleResponse:
    """ Update Parameters Rule Response """

    def __init__(self, _id):
        self.id = _id

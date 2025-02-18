"""_summary_"""
from typing import List
from domain.entities import Case, Condition, KVItem


class CreateCaseRuleRequest:
    """ create a new case """

    def __init__(
            self,
            _id: str,
            name: str,
            case: Case
    ):
        self.id = _id
        self.name = name
        self.case = case

        self.conditions: List[Condition] = []
        self.kvitems: List[KVItem] = []


class CreateCaseRuleResponse:
    """ create a new case response """

    def __init__(self, _id: str):
        self.id = _id

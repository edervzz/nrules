"""_summary_"""
from typing import List
from domain.entities import Case, Rule


class UpdateCaseRuleRequest:
    """ update a case """

    def __init__(
            self,
            _id: str,
            name: str,
            cases: List[Case]
    ):
        self.id = _id
        self.name = name
        self.cases = cases
        self.rule: Rule


class UpdateCaseRuleResponse:
    """ update a case response """

    def __init__(self, _id: str):
        self.id = _id

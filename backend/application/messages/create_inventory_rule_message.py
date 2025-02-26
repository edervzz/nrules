"""_summary_"""
from domain.entities import Rule


class CreateInventoryRuleRequest:
    """ create a new inventory """

    def __init__(
            self,
            _id: str,
            name: str
    ):
        self.id = _id
        self.name = name

        self.rule: Rule


class CreateInventoryRuleResponse:
    """ create a new inventory response """

    def __init__(self, _id: str):
        self.id = _id

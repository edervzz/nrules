""" create rule messages """
from typing import List
from domain.entities import Rule, Parameter


class UpdateRuleRequest:
    """ Update Rule Request """

    def __init__(self, _id: str, name: str, strategy: str):
        self.rule = Rule()
        self.rule.id = _id
        self.rule.name = name
        self.rule.strategy = strategy


class UpdateRuleResponse:
    """ Update Rule Response """

    def __init__(self, _id):
        self.id = _id

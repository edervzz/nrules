""" create rule messages """
from domain.entities import Rule


class UpdateRuleRequest:
    """ Update Rule Request """

    def __init__(self, _id: int, name: str, strategy: str,):
        self.rule = Rule()
        self.rule.id = _id
        self.rule.name = name
        self.rule.strategy = strategy


class UpdateRuleResponse:
    """ Update Rule Response """

    def __init__(self, _id):
        self.id = _id

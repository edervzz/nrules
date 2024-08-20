""" create rule messages """
from domain.entities import Rule


class UpdateRuleRequest:
    """ Update Rule Request """

    def __init__(self, _id: int, name: str, expression: str, is_exclusive: bool):
        self.rule = Rule()
        self.rule.id = _id
        self.rule.name = name
        self.rule.expression = expression
        self.rule.is_exclusive = is_exclusive


class UpdateRuleResponse:
    """ Update Rule Response """

    def __init__(self, _id):
        self.id = _id

""" create rule messages """
from domain.entities import Rule


class CreateRuleRequest:
    """ Create Rule Request """

    def __init__(self, name: str, expression: str, is_exclusive: bool):
        self.rule = Rule()
        self.rule.name = name
        self.rule.expression = expression
        self.rule.is_exclusive = is_exclusive


class CreateRuleResponse:
    """ Create Rule Response """

    def __init__(self, _id):
        self.id = _id

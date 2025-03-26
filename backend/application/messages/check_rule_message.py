""" message """
from domain.entities import Rule


class CheckRuleRequest:
    """ Request """

    def __init__(self, rule_id: int, rule_name: str):
        self.rule_id = rule_id
        self.rule_name = rule_name

        self.rule: Rule = None


class CheckRuleResponse:
    """ Response """

    def __init__(self, ok: bool):
        self.ok = ok

"""_summary_"""


from domain.entities import Rule


class ReadRuleRequest:
    """ Read Rule Request """

    def __init__(self, tenantid: int, rule_id: int = 0, rule_name: str = ""):
        self.tenant_id = tenantid
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule: Rule = None


class ReadRuleResponse:
    """ Read Rule Response """

    def __init__(self, rule: Rule):
        self.rule = rule

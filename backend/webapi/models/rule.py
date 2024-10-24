""" _module_ """


class RuleModel:
    """ Rule Model """

    def __init__(self, tenantid, _id, name, rule_type, strategy, version):
        self.tenant_id = tenantid
        self.id = _id
        self.name = name
        self.rule_type = rule_type
        self.strategy = strategy
        self.version = version

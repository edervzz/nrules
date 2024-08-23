""" _module_ """


class RuleModel:
    """ Rule Model """

    def __init__(self, tenantid, _id, name, expression, is_exclusive, version):
        self.tenant_id = tenantid
        self.id = _id
        self.name = name
        self.expression = expression
        self.is_exclusive = is_exclusive
        self.version = version

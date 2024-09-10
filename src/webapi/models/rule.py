""" _module_ """


class RuleModel:
    """ Rule Model """

    def __init__(self, tenantid, _id, name, is_zero_condition, kvs_id, version):
        self.tenant_id = tenantid
        self.id = _id
        self.name = name
        self.is_zero_condition = is_zero_condition
        self.kvs_id = kvs_id
        self.version = version

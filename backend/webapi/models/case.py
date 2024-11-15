class CaseModel:
    """ Case Model """

    def __init__(self, _id, rule_id, position, condition_group_id, kvs_id):
        self.id = _id
        self.rule_id = rule_id
        self.position = position
        self.condition_group_id = condition_group_id
        self.kvs_id = kvs_id

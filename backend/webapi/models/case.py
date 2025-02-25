""" _module_ """


class CaseModel:
    """ Case Model """

    def __init__(self, _id, rule_id, position, is_active, is_archived):
        self.id = _id
        self.rule_id = rule_id
        self.position = position
        self.is_active = is_active
        self.is_archived = is_archived

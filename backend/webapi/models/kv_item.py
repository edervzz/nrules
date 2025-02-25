""" _module_ """


class KVItemModel:
    """ KV Item Model """

    def __init__(self, key, case_id, rule_id, value, calculation):
        self.key = key
        self.case_id = case_id
        self.rule_id = rule_id
        self.value = value
        self.calculation = calculation

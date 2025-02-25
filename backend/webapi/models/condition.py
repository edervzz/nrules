""" _module_ """


class ConditionModel:
    """ Condition Model """

    def __init__(self, variable, case_id, rule_id, operator, value):
        self.variable = variable
        self.case_id = case_id
        self.rule_id = rule_id
        self.operator = operator
        self.value = value

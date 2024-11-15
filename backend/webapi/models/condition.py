class ConditionModel:
    """ Condition  Model """

    def __init__(self, variable, condition_group_id, operator, value, is_case_sensitive, typeof):
        self.variable = variable
        self.condition_group_id = condition_group_id
        self.operator = operator
        self.value = value
        self.is_case_sensitive = is_case_sensitive
        self.typeof = typeof

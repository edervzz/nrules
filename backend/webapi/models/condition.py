""" _module_ """


class ConditionModel:
    """ Condition Model """

    def __init__(self, variable, condition_group_id, operator, value,  typeof, is_active):
        self.variable = variable
        self.condition_group_id = condition_group_id
        self.operator = operator
        self.value = value
        self.typeof = typeof
        self.is_active = is_active

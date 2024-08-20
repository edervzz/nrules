""" _module_ """


class RuleModel:
    """ Rule Model """

    def __init__(self, name, expression, is_exclusive):
        self.name = name
        self.expression = expression
        self.is_exclusive = is_exclusive

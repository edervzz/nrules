""" _module_ """


class RuleModel:
    """ Rule Model """

    def __init__(self, _id, name, expression, is_exclusive):
        self.id = _id
        self.name = name
        self.expression = expression
        self.is_exclusive = is_exclusive

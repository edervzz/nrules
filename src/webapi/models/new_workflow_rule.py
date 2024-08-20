""" models """


class NewWorkflowRuleModel:
    """ New Rule request """

    def __init__(self, name: str, operator: str, expression: str):
        self.name: str = name
        self.operator: str = operator
        self.expression: str = expression

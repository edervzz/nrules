""" Entities """


class RuleInventory():
    """ Rule Inventory entity.
    """

    def __init__(self, rule, cases, conditions, kvitems, parameters, tags):
        self.rule = rule
        self.cases = cases
        self.conditions = conditions
        self.kvitems = kvitems
        self.parameters = parameters
        self.tags = tags

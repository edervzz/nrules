""" _module_ """


class ParameterModel:
    """ Parameter Model """

    def __init__(self, key: str, rule_id: str, usefor: str, typeof: str):
        self.key = key
        self.rule_id = rule_id
        self.usefor = usefor
        self.typeof = typeof

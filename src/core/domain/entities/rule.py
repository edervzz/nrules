"""  """


class Rule:
    """ Rule entity """
    id: int
    name: str
    expression: str

    def __ini__(self, id_: int, name: str, expression: str):
        self.id = id_
        self.name = name
        self.expression = expression

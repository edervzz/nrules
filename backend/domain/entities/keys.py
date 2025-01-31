""" Keys """


class LockKey:
    """ Lock Key """

    def __init__(self, tablename: str, argument: str):
        self.tablename = tablename
        self.argument = argument


class KVItemKey:
    """ KV Item Key """

    def __init__(self, case_id: int, key: str):
        self.case_id = case_id
        self.key = key


class ParameterKey:
    """ Parameter Key """

    def __init__(self, rule_id: str, key: str, usefor: str):
        self.rule_id = rule_id
        self.key = key
        self.usefor = usefor


class HistoricalKey:
    """ Historical Key """

    def __init__(self, objtype: str, objid: int, objver: int):
        self.objtype = objtype
        self.objid = objid
        self.objver = objver


class ConditionKey:
    """ Condition Key """

    def __init__(self, variable: str, case_id: str) -> None:
        self.variable = variable
        self.case_id = case_id

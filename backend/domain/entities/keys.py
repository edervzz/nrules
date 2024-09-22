""" Keys """


class KVItemKey:
    """ KV Item Key """

    def __init__(self, kvid: int, key: int):
        self.kv_id = kvid
        self.key = key


class HistoricalKey:
    """ Historical Key """

    def __init__(self, objtype: str, objid: int, objver: int):
        self.objtype = objtype
        self.objid = objid
        self.objver = objver

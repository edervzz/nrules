""" _module_ """


class KVItemModel:
    """ KV Item Model """

    def __init__(self, key, kv_id, value, calculation, typeof, is_active):
        self.key = key
        self.kv_id = kv_id
        self.value = value
        self.calculation = calculation
        self.typeof = typeof
        self.is_active = is_active

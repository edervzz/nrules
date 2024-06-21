""" _summry_ """


class KeyValue:
    """ Key Value Type """

    def __init__(self, name: str, value, value_type: str):
        self.key = name
        self.value = value
        self.value_type = value_type


class Variable:
    """ Variable """

    def __init__(self, kv: KeyValue):
        self.key_value = kv


class KVS:
    """ Key Value Storage """

    def __init__(self, kv: KeyValue):
        self.key_value = kv

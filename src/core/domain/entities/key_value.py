""" _summry_ """


class KeyValue:
    """ Key Value Type """
    key: str
    value: object
    value_type: str


class Variable:
    """ Variable """
    key_value: KeyValue


class KVS:
    """ Key Value Storage """
    key_value: KeyValue

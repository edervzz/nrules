""" Rule Set module """

from typing import List


class NewRuleSet:
    """ New Rule Set request """
    name: str
    rules: List[int]


class NewRuleSetResult:
    """ Rule Set Response """
    id: int

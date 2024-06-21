""" Operators """
from typing import List


def get_inner_operators() -> List[str]:
    """ get operators for expression"""
    return ["EQ", "NE", "LT", "LE", "GT", "GE", "IN", "NI"]


def get_operators() -> List[str]:
    """ get operators between rules, rule sets"""
    return ["AND", "OR"]

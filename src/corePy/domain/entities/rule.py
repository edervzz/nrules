""" _summary_ """
from typing import List
from domain.entities.oper import get_operators


class Rule:
    """_summary_"""

    def __init__(self):
        self.params = []
        self.expression: str = ""
        self.operators: List[str] = get_operators()

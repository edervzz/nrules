"""_summary_"""

from typing import List
from domain.entities import Rule, Pagination


class ReadAllRulesRequest:
    """ Read Rules Request """

    def __init__(self, page_no: int, page_size: int):
        self.page_no = page_no
        self.page_size = page_size
        self.rules: List[Rule]
        self.pagination: Pagination


class ReadAllRulesResponse:
    """ Read Rules Response """

    def __init__(self, rules: List[Rule], pagination: Pagination):
        self.rules = rules
        self.pagination = pagination

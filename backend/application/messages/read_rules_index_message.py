"""_summary_"""

from typing import List
from domain.entities import Rule, Pagination


class ReadRulesByKeyIndexRequest:
    """ Read Rules Request """

    def __init__(self, tenant_id: int, key: str, page_no: int, page_size: int):
        self.tenant_id = tenant_id
        self.page_no = page_no
        self.page_size = page_size
        self.key = key
        self.rules: List[Rule]
        self.pagination: Pagination


class ReadRulesByKeyIndexResponse:
    """ Read Rules Response """

    def __init__(self, rules: List[Rule], pagination: Pagination):
        self.rules = rules
        self.pagination = pagination

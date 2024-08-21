"""_summary_"""
import logging
from application.messages import ReadAllRulesRequest, ReadAllRulesResponse
from application.validators import ReadAllRulesValidator
from domain.entities import Pagination
from domain.ports import Repository
from toolkit import Localizer


class ReadAllRulesHandler:
    """ Read All Rules Handler """

    def __init__(self, repository: Repository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer

    def handler(self, request: ReadAllRulesRequest) -> ReadAllRulesResponse:
        """ Handler """
        # 1. request validation
        validator = ReadAllRulesValidator(self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("request validated")

        rules, pagination = self.repository.rule.read_page(
            request.page_no, request.page_size)

        # todo: move to biz validator
        if not isinstance(pagination, Pagination):
            raise TypeError("type error: Pagination")

        return ReadAllRulesResponse(rules, pagination)

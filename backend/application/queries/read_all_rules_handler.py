"""_summary_"""
import logging
from application.messages import ReadAllRulesRequest, ReadAllRulesResponse
from application.validators import ReadAllRulesValidator, ReadAllRulesBizValidator
from domain.entities import Pagination
from domain.ports import CoreRepository
from toolkit import Localizer


class ReadAllRulesHandler:
    """ Read All Rules Handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer

    def handler(self, request: ReadAllRulesRequest) -> ReadAllRulesResponse:
        """ Handler """
        # 1. request validation
        validator = ReadAllRulesValidator(self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("request validated")

        validator = ReadAllRulesBizValidator(self.repository, self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("request validated")

        if not isinstance(request.pagination, Pagination):
            raise TypeError("type error: Pagination")

        return ReadAllRulesResponse(request.rules, request.pagination)

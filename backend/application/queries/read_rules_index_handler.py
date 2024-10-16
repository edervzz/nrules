"""_summary_"""
import logging
from application.messages import ReadRulesByKeyIndexRequest, ReadRulesByKeyIndexResponse
from application.validators import ReadRulesKeyIndexValidator, ReadAllRulesBizValidator
from domain.entities import Pagination
from domain.ports import CoreRepository
from toolkit import Localizer


class ReadRulesKeyIndexHandler:
    """ Read Rules by key index Handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer

    def handler(self, request: ReadRulesByKeyIndexRequest):
        """ Handler """
        # 1. request validation
        validator = ReadRulesKeyIndexValidator(self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("request validated")
        # 2. business ruless validation
        validator = ReadAllRulesBizValidator(self.repository, self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("business rules validated")

        if not isinstance(request.pagination, Pagination):
            raise TypeError("type error: Pagination")

        return ReadRulesByKeyIndexResponse(request.rules, request.pagination)

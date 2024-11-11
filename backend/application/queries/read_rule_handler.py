"""_summary_"""
import logging
from application.messages import ReadRuleRequest, ReadRuleResponse
from application.validators import ReadRuleValidator, ReadRuleBizValidator
from domain.ports import CoreRepository
from toolkit import Localizer


class ReadRuleHandler:
    """ Read Rule Handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer

    def handler(self, request: ReadRuleRequest) -> ReadRuleResponse:
        """ Handler """
        # 1. request validation
        validator = ReadRuleValidator(self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("request validated")
        # 2. business rule validation
        biz_validator = ReadRuleBizValidator(self.repository, self.localizer)
        biz_validator.validate_and_throw(request)
        self.logger.info("business rules validated")

        return ReadRuleResponse(request.rule, request.cases, request.parameters, request.conditions, request.kvs_items)

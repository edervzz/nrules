r"""_summary_"""
import logging
from application.messages import CheckRuleRequest, CheckRuleResponse
from application.validators import CheckRuleValidator, CheckRuleBizValidator
from domain.ports import CoreRepository
from toolkit import Localizer


class CheckRuleHandler:
    """ command """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer

    def handler(self, request: CheckRuleRequest):
        """ Handler """
        # 1. request validation
        validator = CheckRuleValidator(self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("request validated")
        # 2. business rule validation
        biz_validator = CheckRuleBizValidator(self.repository, self.localizer)
        biz_validator.validate_and_throw(request)
        self.logger.info("business rules validated")

        return CheckRuleResponse(True)

r"""_summary_"""
import logging
from application.messages import RunRuleRequest, RunRuleResponse
from application.validators import RunRuleValidator, RunRuleBizValidator
from domain.ports import CoreRepository
from toolkit import Localizer


class RunRuleHandler:
    """ command """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer

    def handler(self, request: RunRuleRequest):
        """ Handler """
        # 1. request validation
        validator = RunRuleValidator(self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("request validated")
        # 2. business rule validation
        biz_validator = RunRuleBizValidator(self.repository, self.localizer)
        biz_validator.validate_and_throw(request)
        self.logger.info("business rules validated")

        return RunRuleResponse(request.ok, request.rule_results, request.trace)

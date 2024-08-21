r"""_summary_"""
import logging
from application.messages import UpdateRuleRequest, UpdateRuleResponse
from application.validators import UpdateRuleValidator, UpdateRuleBizValidator
from domain.ports import Repository
from domain.entities import Rule
from toolkit import Localizer


class UpdateRuleHandler:
    """ Update Rule Handler """

    def __init__(self, repository: Repository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer
        self.rule: Rule = None

    def handler(self, request: UpdateRuleRequest) -> UpdateRuleResponse:
        """ Handler """
        # 1. request validation
        validator = UpdateRuleValidator(self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("request validated")
        # 2. business rule validation
        biz_validator = UpdateRuleBizValidator(self.repository, self.localizer)
        biz_validator.validate_and_throw(request)
        self.logger.info("business rules validated")

        self.repository.begin()
        self.repository.rule.update(request.rule)
        self.repository.commit_work()

        return UpdateRuleResponse(request.rule.id)

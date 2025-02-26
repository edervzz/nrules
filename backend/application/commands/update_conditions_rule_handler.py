r"""_summary_"""
import logging
from application.messages import UpdateConditionsRuleRequest, UpdateConditionsRuleResponse
from application.validators import UpdateConditionsRuleBizValidator, UpdateConditionsRuleValidator
from domain.ports import CoreRepository
from domain.entities import Rule
from toolkit import Localizer


class UpdateConditionsRuleHandler:
    """ Update Conditions Handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repo = repository
        self.log = logger
        self.local = localizer
        self.rule: Rule = None

    def handler(self, request: UpdateConditionsRuleRequest):
        """ Handler """
        # 1. request validation
        validator = UpdateConditionsRuleValidator(self.local)
        validator.validate_and_throw(request)
        self.log.info("request validated")
        # 2. business rule validation
        biz_validator = UpdateConditionsRuleBizValidator(self.repo, self.local)
        biz_validator.validate_and_throw(request)
        self.log.info("business rules validated")

        self.repo.begin()

        if len(request.income_conditions) > 0:
            for e in request.income_conditions:
                self.repo.condition.update(e)

        self.repo.rule.update(request.rule)

        self.repo.commit_work()

        return UpdateConditionsRuleResponse(request.id)

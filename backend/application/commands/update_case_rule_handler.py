""" summary """
import logging
from application.messages import UpdateCaseRuleRequest, UpdateCaseRuleResponse
from application.validators import UpdateCaseRuleValidator, UpdateCaseRuleBizValidator
from domain.ports import CoreRepository
from domain.entities import Case
from toolkit import Localizer


class UpdateCaseRuleHandler:
    """ update case rule handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repo = repository
        self.log = logger
        self.local = localizer
        self.case: Case = None

    def handler(self, request: UpdateCaseRuleRequest):
        """ handler """
        # 1. request validation
        validator = UpdateCaseRuleValidator(self.local)
        validator.validate_and_throw(request)
        self.log.info("request validated")
        # 2. business rule validation
        biz_validator = UpdateCaseRuleBizValidator(self.repo, self.local)
        biz_validator.validate_and_throw(request)
        self.log.info("business rules validated")

        self.repo.begin()

        for c in request.cases:
            self.repo.case.update(c)

        self.repo.rule.update(request.rule)

        self.repo.commit_work()

        return UpdateCaseRuleResponse(request.rule.id)

""" summary """
import logging
from application.messages import CreateCaseRuleRequest, CreateCaseRuleResponse
from application.validators import CreateCaseRuleValidator, CreateCaseRuleBizValidator
from domain.ports import CoreRepository
from domain.entities import Case
from toolkit import Localizer


class CreateCaseRuleHandler:
    """ create case rule handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repo = repository
        self.log = logger
        self.local = localizer
        self.case: Case = None

    def handler(self, request: CreateCaseRuleRequest):
        """ handler """
        # 1. request validation
        validator = CreateCaseRuleValidator(self.local)
        validator.validate_and_throw(request)
        self.log.info("request validated")
        # 2. business rule validation
        biz_validator = CreateCaseRuleBizValidator(self.repo, self.local)
        biz_validator.validate_and_throw(request)
        self.log.info("business rules validated")

        self.repo.begin()

        self.repo.case.create(request.case)

        for c in request.conditions:
            self.repo.condition.create(c)

        for k in request.kvitems:
            self.repo.kvitem.create(k)

        self.repo.commit_work()

        return CreateCaseRuleResponse(request.case.id)

""" summary """
import logging
from application.messages import CreateInventoryRuleRequest, CreateInventoryRuleResponse
from application.validators import CreateInventoryRuleValidator, CreateInventoryRuleBizValidator
from domain.ports import CoreRepository
from domain.entities import Case
from toolkit import Localizer


class CreateInventoryRuleHandler:
    """ create case rule handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repo = repository
        self.log = logger
        self.local = localizer
        self.case: Case = None

    def handler(self, request: CreateInventoryRuleRequest):
        """ handler """
        # 1. request validation
        validator = CreateInventoryRuleValidator(self.local)
        validator.validate_and_throw(request)
        self.log.info("request validated")
        # 2. business rule validation
        biz_validator = CreateInventoryRuleBizValidator(self.repo, self.local)
        biz_validator.validate_and_throw(request)
        self.log.info("business rules validated")

        return CreateInventoryRuleResponse(request.rule.id)

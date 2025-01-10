r"""_summary_"""
import logging
from application.messages import CreateConditionsRuleRequest, CreateConditionsRuleResponse
from application.validators import CreateConditionsRuleValidator, CreateConditionsRuleBizValidator
from domain.ports import CoreRepository
from domain.entities import Rule
from toolkit import Localizer


class CreateConditionsRuleHandler:
    """ Create Conditions Handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repo = repository
        self.log = logger
        self.local = localizer
        self.rule: Rule = None

    def handler(self, request: CreateConditionsRuleRequest) -> CreateConditionsRuleResponse:
        """ Handler """
        # 1. request validation
        validator = CreateConditionsRuleValidator(self.local)
        validator.validate_and_throw(request)
        self.log.info("request validated")
        # 2. business rule validation
        biz_validator = CreateConditionsRuleBizValidator(self.repo, self.local)
        biz_validator.validate_and_throw(request)
        self.log.info("business rules validated")

        self.repo.begin()

        if len(request.new_parameters) > 0:
            for e in request.new_parameters:
                self.repo.parameter.create(e)

        if len(request.new_conditions) > 0:
            for e in request.new_conditions:
                self.repo.condition.create(e)

        self.repo.commit_work()

        return CreateConditionsRuleResponse(request.id)

r"""_summary_"""
import logging
from application.messages import CreateParamtersRuleRequest, CreateParametersRuleResponse
from application.validators import CreateParametersRuleValidator, CreateParametersRuleBizValidator
from domain.ports import CoreRepository
from domain.entities import Rule
from toolkit import Localizer


class CreateParametersRuleHandler:
    """ Create Parameters Handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repo = repository
        self.log = logger
        self.local = localizer
        self.rule: Rule = None

    def handler(self, request: CreateParamtersRuleRequest) -> CreateParametersRuleResponse:
        """ Handler """
        # 1. request validation
        validator = CreateParametersRuleValidator(self.local)
        validator.validate_and_throw(request)
        self.log.info("request validated")
        # 2. business rule validation
        biz_validator = CreateParametersRuleBizValidator(self.repo, self.local)
        biz_validator.validate_and_throw(request)
        self.log.info("business rules validated")

        self.repo.begin()

        if len(request.parameters) > 0:
            for e in request.parameters:
                self.repo.parameter.create(e)

        if len(request.conditions) > 0:
            for e in request.conditions:
                self.repo.condition.create(e)

        if len(request.kvitems) > 0:
            for e in request.kvitems:
                self.repo.kvitem.create(e)

        self.repo.commit_work()

        return CreateParametersRuleResponse(request.id)

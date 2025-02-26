r"""_summary_"""
import logging
from application.messages import UpdateParametersRuleRequest, UpdateParametersRuleResponse
from application.validators import UpdateParametersRuleValidator, UpdateParametersRuleBizValidator
from domain.ports import CoreRepository
from domain.entities import Rule
from toolkit import Localizer


class UpdateParamtersRuleHandler:
    """ Update Parameters Handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repo = repository
        self.log = logger
        self.local = localizer
        self.rule: Rule = None

    def handler(self, request: UpdateParametersRuleRequest) -> UpdateParametersRuleResponse:
        """ Handler """
        # 1. request validation
        validator = UpdateParametersRuleValidator(self.local)
        validator.validate_and_throw(request)
        self.log.info("request validated")
        # 2. business rule validation
        biz_validator = UpdateParametersRuleBizValidator(self.repo, self.local)
        biz_validator.validate_and_throw(request)
        self.log.info("business rules validated")

        self.repo.begin()

        if len(request.parameters) > 0:
            for e in request.parameters:
                self.repo.parameter.update(e)

        self.repo.rule.update(request.rule)

        self.repo.commit_work()

        return UpdateParametersRuleResponse(request.id)

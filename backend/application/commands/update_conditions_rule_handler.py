r"""_summary_"""
import logging
from application.messages import UpdateConditionsRuleRequest, UpdateConditionsRuleResponse
from application.validators import UpdateConditionsRuleValidator, UpdateConditionsRuleBizValidator
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

    def handler(self, request: UpdateConditionsRuleRequest) -> UpdateConditionsRuleResponse:
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

        if len(request.upd_conditions) > 0:
            for e in request.upd_conditions:
                self.repo.condition.update(e)
        if len(request.upd_parameters) > 0:
            for e in request.upd_parameters:
                self.repo.parameter.update(e)

        self.repo.commit_work()

        return UpdateConditionsRuleResponse(request.id)

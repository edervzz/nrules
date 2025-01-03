r"""_summary_"""
import logging
from application.messages import SaveConditionsRuleRequest, SaveConditionsRuleResponse
from application.validators import SaveConditionsRuleValidator, SaveConditionsRuleBizValidator
from domain.ports import CoreRepository
from domain.entities import Rule
from toolkit import Localizer


class SaveConditionsRuleHandler:
    """ Save Conditions Handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repo = repository
        self.log = logger
        self.local = localizer
        self.rule: Rule = None

    def handler(self, request: SaveConditionsRuleRequest) -> SaveConditionsRuleResponse:
        """ Handler """
        # 1. request validation
        validator = SaveConditionsRuleValidator(self.local)
        validator.validate_and_throw(request)
        self.log.info("request validated")
        # 2. business rule validation
        biz_validator = SaveConditionsRuleBizValidator(self.repo, self.local)
        biz_validator.validate_and_throw(request)
        self.log.info("business rules validated")

        self.repo.begin()

        if len(request.insert_cond_parameters) > 0:
            for e in request.insert_cond_parameters:
                self.repo.condition.create(e)
        if len(request.insert_parameters) > 0:
            for e in request.insert_parameters:
                self.repo.parameter.create(e)

        if len(request.update_cond_parameters) > 0:
            for e in request.update_cond_parameters:
                self.repo.condition.update(e)

        if len(request.update_parameters) > 0:
            for e in request.update_parameters:
                self.repo.parameter.update(e)

        self.repo.commit_work()

        return SaveConditionsRuleResponse(request.rule.id)

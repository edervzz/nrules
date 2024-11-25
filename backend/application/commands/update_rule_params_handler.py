"""_summary_
    """
import logging
from application.messages import UpdateRuleParamsRequest, UpdateRuleParamsResponse
from application.validators import UpdateRuleParamsValidator, UpdateRuleParamsBizValidator
from domain.ports import CoreRepository
from toolkit import Localizer


class UpdateRuleParamsHandler:
    """ Save Condition Parameters Handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer

    def handler(self, request: UpdateRuleParamsRequest):
        """handler"""
        # 1. request validation
        validator = UpdateRuleParamsValidator(self.localizer)
        validator.validate_and_throw(request)
        # 2. business rule validation
        biz_validator = UpdateRuleParamsBizValidator(
            self.repository, self.localizer)
        biz_validator.validate_and_throw(request)

        self.repository.begin()
        if len(request.parameters_to_insert) > 0:
            for x in request.parameters_to_insert:
                self.repository.parameter.create(x)

        if len(request.parameters_to_update) > 0:
            for x in request.parameters_to_update:
                self.repository.parameter.update(x)

        if len(request.conditions_to_insert) > 0:
            for x in request.conditions_to_insert:
                self.repository.condition.create(x)

        if len(request.conditions_to_update) > 0:
            for x in request.conditions_to_update:
                self.repository.condition.update(x)

        if len(request.output_to_insert) > 0:
            for x in request.output_to_insert:
                self.repository.kvitem.create(x)

        if len(request.output_to_update) > 0:
            for x in request.output_to_update:
                self.repository.kvitem.update(x)

        self.repository.commit_work()

        return UpdateRuleParamsResponse(request.rule.id)

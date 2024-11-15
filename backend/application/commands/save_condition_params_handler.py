"""_summary_
    """
import logging
from application.messages import SaveConditionParamsRequest, SaveConditionParamsResponse
from application.validators import SaveConditionsParamsValidator, SaveConditionParamsBizValidator
from domain.ports import CoreRepository
from domain.entities import Parameter
from toolkit import Localizer


class SaveConditionParamsHandler:
    """ Save Condition Parameters Handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer

    def handler(self, request: SaveConditionParamsRequest):
        """handler"""
        # 1. request validation
        validator = SaveConditionsParamsValidator(self.localizer)
        validator.validate_and_throw(request)
        # 2. business rule validation
        biz_validator = SaveConditionParamsBizValidator(
            self.repository, self.localizer)
        biz_validator.validate_and_throw(request)

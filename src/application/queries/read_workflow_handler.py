"""_summary_
    """
import logging
from application.messages import ReadWorkflowRequest, ReadWorkflowResponse
from application.validators import ReadWorkflowValidator, ReadWorkflowBizValidator
from domain.ports import CoreRepository
from toolkit import Localizer


class ReadWorkflowHandler:
    """ _summary_ """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer

    def handler(self, request: ReadWorkflowRequest):
        """ Handler """
        # 1. request validation
        validator = ReadWorkflowValidator(self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("request validated")

        # 2. business rule validation
        biz_validator = ReadWorkflowBizValidator(
            self.repository, self.localizer)
        biz_validator.validate_and_throw(request)
        self.logger.info("business rules validated")

        return ReadWorkflowResponse(request.workflow, request.rules)

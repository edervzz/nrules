"""_summary_
    """
import logging
from application.messages import ReadWorkflowRequest, ReadWorkflowResponse
from application.validators import ReadWorkflowValidator, ReadWorkflowBizValidator
from domain.ports import Repository


class ReadWorkflowHandler:
    """ _summary_ """

    def __init__(self, repository: Repository, logger: logging):
        self.repository = repository
        self.logger = logger

    def handler(self, request: ReadWorkflowRequest) -> ReadWorkflowResponse:
        """ Handler """
        # 1. request validation
        validator = ReadWorkflowValidator()
        validator.validate_and_throw(request)
        self.logger.info("request validated")

        # 2. business rule validation
        biz_validator = ReadWorkflowBizValidator(self.repository)
        biz_validator.validate_and_throw(request)
        self.logger.info("business rules validated")

        return ReadWorkflowResponse(request.workflow, request.rules)

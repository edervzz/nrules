"""_summary_
    """
import logging
from application.messages import CreateWorkflowRequest, CreateWorkflowResponse
from application.validators import CreateWorkflowValidator, CreateWorkflowBizValidator
from domain.ports import Repository
from domain.entities import Workflow


class CreateWorkflowHandler:
    """ _summary_ """

    def __init__(self, repository: Repository, logger: logging):
        self.repository = repository
        self.logger = logger
        self.workflow: Workflow = None

    def handler(self, request: CreateWorkflowRequest) -> CreateWorkflowResponse:
        """ Handler """
        # 1. request validation
        validator = CreateWorkflowValidator(request)
        validator.validate()
        self.logger.info("request validated")
        # 2. business rule validation
        biz_validator = CreateWorkflowBizValidator(request)
        biz_validator.validate(self.repository)
        self.logger.info("business rules validated")

        self.repository.begin()
        self.repository.create(request.workflow)
        self.repository.create(request.rules)
        self.repository.commit_work()
        self.logger.info(request.workflow.id)

        return CreateWorkflowResponse(request.workflow.id)

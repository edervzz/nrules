"""_summary_
    """
import logging
from application.messages import CreateWorkflowRequest, CreateWorkflowResponse
from application.validators import CreateWorkflowValidator, CreateWorkflowBizValidator
from domain.ports import Repository
from domain.entities import Workflow, WorkflowRule


class CreateWorkflowHandler:
    r""" _summary_ """

    def __init__(self, repository: Repository, logger: logging):
        self.repository = repository
        self.logger = logger
        self.workflow: Workflow = None

    def handler(self, request: CreateWorkflowRequest) -> CreateWorkflowResponse:
        r""" Handler """
        # 1. request validation
        validator = CreateWorkflowValidator()
        validator.validate_and_throw(request)
        self.logger.info("request validated")
        # 2. business rule validation
        biz_validator = CreateWorkflowBizValidator(self.repository)
        biz_validator.validate_and_throw(request)
        self.logger.info("business rules validated")

        self.repository.begin()
        self.repository.create(request.workflow)

        for r in request.rules:
            self.repository.create(r)

            wfr = WorkflowRule()
            wfr.workflow_id = request.workflow.id
            wfr.rule_id = r.id
            self.repository.create(wfr)

        self.repository.commit_work()
        self.logger.info(request.workflow.id)

        return CreateWorkflowResponse(request.workflow.id)

""" summary """
import logging
from application.messages import CreateNodeRuleRequest, CreateNodeRuleResponse
from application.messages import CreateCaseRuleRequest, CreateCaseRuleResponse
from application.validators import CreateNodeRuleValidator, CreateNodeRuleBizValidator
from application.validators import CreateCaseRuleValidator, CreateCaseRuleBizValidator
from domain.ports import CoreRepository
from domain.entities import Case
from toolkit import Localizer


class CreateNodeRuleHandler:
    """ create case rule handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repo = repository
        self.log = logger
        self.local = localizer
        self.case: Case = None

    def handler(self, request: CreateNodeRuleRequest):
        """ handler """
        # 1. request validation
        validator = CreateNodeRuleValidator(self.local)
        validator.validate_and_throw(request)
        self.log.info("request validated")
        # 2. business rule validation
        biz_validator = CreateNodeRuleBizValidator(self.repo, self.local)
        biz_validator.validate_and_throw(request)
        self.log.info("business rules validated")
        # 3. request for case
        case_request = CreateCaseRuleRequest(
            request.rule.id,
            request.rule.name,
            request.case)
        # 4. business rule validation for case
        case_biz_validator = CreateCaseRuleBizValidator(
            self.repo, self.local, from_node=True)
        case_biz_validator.validate_and_throw(case_request)
        self.log.info("business rules validated (case)")

        self.repo.begin()

        self.repo.case.create(case_request.case)

        for c in case_request.conditions:
            self.repo.condition.create(c)

        for k in case_request.kvitems:
            self.repo.kvitem.create(k)

        self.repo.node.create(request.new_node)
        self.repo.node.update(request.parent_node)

        self.repo.rule.update(request.rule)

        self.repo.commit_work()

        return CreateNodeRuleResponse(request.case.id)

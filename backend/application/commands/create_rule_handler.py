r"""_summary_"""
import logging
from application.messages import CreateRuleRequest, CreateRuleResponse
from application.validators import CreateRuleValidator, CreateRuleBizValidator
from domain.ports import CoreRepository
from domain.entities import Rule
from toolkit import Localizer


class CreateRuleHandler:

    """ Create a new rule """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer
        self.rule: Rule = None

    def handler(self, request: CreateRuleRequest) -> CreateRuleResponse:
        r""" Handler """
        # 1. request validation
        validator = CreateRuleValidator(self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("request validated")
        # 2. business rule validation
        biz_validator = CreateRuleBizValidator(
            self.repository, self.logger, self.localizer)
        biz_validator.validate_and_throw(request)
        self.logger.info("business rules validated")

        self.repository.begin()

        self.repository.rule.create(request.rule)
        self.repository.kvs.create(request.default_kvs)
        self.repository.case.create(request.default_case)

        self.repository.condition_group.create(request.condition_group)
        for x in request.conditions:
            self.repository.condition.create(x)

        self.repository.kvs.create(request.kvs)
        for x in request.kv_items:
            self.repository.kvitem.create(x)

        for x in request.parameters:
            self.repository.parameter.create(x)

        if len(request.tags) > 0:
            for x in request.tags:
                self.repository.tag.create(x)

        self.repository.commit_work()

        return CreateRuleResponse(request.rule.id)

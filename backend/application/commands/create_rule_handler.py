r"""_summary_"""
import logging
from application.messages import CreateRuleRequest, CreateRuleResponse
from application.validators import CreateRuleValidator, CreateRuleBizValidator
from domain.ports import CoreRepository
from domain.entities import Rule
from toolkit import Localizer


class CreateRuleHandler:
    """ Create a new Rule """

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
        biz_validator = CreateRuleBizValidator(self.repository, self.localizer)
        biz_validator.validate_and_throw(request)
        self.logger.info("business rules validated")

        self.repository.begin()

        if request.use_default:
            self.repository.kv_storage.create(request.default_kvs)

        self.repository.condition_group.create(request.condition_group)
        for x in request.conditions:
            self.repository.condition.create(x)

        self.repository.kv_storage.create(request.kvs)
        for x in request.kv_items:
            self.repository.kvitem.create(x)

        self.repository.rule.create(request.rule)

        self.repository.case.create(request.case)

        for x in request.parameters:
            self.repository.parameter.create(x)

        self.repository.commit_work()

        return CreateRuleResponse(request.rule.id)

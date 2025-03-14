r"""_summary_"""
import logging
from application.messages import UpdateKVItemsRuleRequest, UpdateKVItemsRuleResponse
from application.validators import UpdateKVItemsRuleBizValidator, UpdateKVItemsRuleValidator
from domain.ports import CoreRepository
from domain.entities import Rule
from toolkit import Localizer


class UpdateKVItemsRuleHandler:
    """ Update KV Items Handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repo = repository
        self.log = logger
        self.local = localizer
        self.rule: Rule = None

    def handler(self, request: UpdateKVItemsRuleRequest):
        """ Handler """
        # 1. request validation
        validator = UpdateKVItemsRuleValidator(self.local)
        validator.validate_and_throw(request)
        self.log.info("request validated")
        # 2. business rule validation
        biz_validator = UpdateKVItemsRuleBizValidator(self.repo, self.local)
        biz_validator.validate_and_throw(request)
        self.log.info("business rules validated")

        self.repo.begin()

        if len(request.income_kvitems) > 0:
            for e in request.income_kvitems:
                self.repo.kvitem.update(e)

        self.repo.rule.update(request.rule)

        self.repo.commit_work()

        return UpdateKVItemsRuleResponse(request.id)

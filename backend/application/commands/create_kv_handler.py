r"""_summary_"""
import logging
from application.messages import CreateKVRequest, CreateKVResponse
from application.validators import CreateKVValidator, CreateKVBizValidator
from domain.ports import CoreRepository
from toolkit import Localizer


class CreateKVHandler:
    r""" _summary_ """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer

    def handler(self, request: CreateKVRequest):
        r""" Handler """
        # 1. request validation
        validator = CreateKVValidator(self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("request validated")
        # 2. business rule validation
        biz_validator = CreateKVBizValidator(self.repository, self.localizer)
        biz_validator.validate_and_throw(request)
        self.logger.info("business rules validated")

        self.repository.begin()
        self.repository.rule.create(request.kv)
        self.repository.commit_work()

        return CreateKVResponse(request.kv.id)

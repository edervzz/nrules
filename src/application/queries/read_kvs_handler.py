""" KVS Handler """
import logging
from domain.ports import CoreRepository
from toolkit import Localizer
from application.messages import ReadKVSRequest, ReadKVSResponse
from application.validators import ReadKVSValidator, ReadKVSBizValidator


class ReadKVSHandler:
    """_summary_
    """

    def __init__(self, repo: CoreRepository, local: Localizer, log: logging) -> None:
        self.repo = repo
        self.local = local
        self.log = log

    def handler(self, request: ReadKVSRequest):
        """Handler"""
        # 1. request validation
        validator = ReadKVSValidator(self.local)
        validator.validate_and_throw(request)
        self.log.info("request validated")
        # 2. business rule validation
        biz_validator = ReadKVSBizValidator(self.repo, self.local)
        biz_validator.validate_and_throw(request)
        self.log.info("business rules validation")
        # return ReadKVSResponse(kvs, kvitems)

        return ReadKVSResponse(request.kv, request.kvitems)

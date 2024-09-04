"""_summary_
    """
import logging
from toolkit import Localizer
from domain.ports import CoreRepository
from application.messages import SaveKVItemRequest, SaveKVItemResponse
from application.validators import SaveKVItemValidator, SaveKVItemBizValidator


class SaveKVItemHandler:
    """ KV Item Handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer

    def handler(self, request: SaveKVItemRequest):
        """ Handler """
        # 1. request validation
        validator = SaveKVItemValidator(self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("request validated")
        # 2. business rule validation
        biz_validator = SaveKVItemBizValidator(self.repository, self.localizer)
        biz_validator.validate_and_throw(request)
        self.logger.info("business rules validated")

        self.repository.begin()
        if len(request.kvitems_to_update) > 0:
            for it in request.kvitems_to_update:
                self.repository.kvitem.update(it)
        if len(request.kvitems_to_insert) > 0:
            for it in request.kvitems_to_insert:
                self.repository.kvitem.create(it)
        self.repository.commit_work()

        return SaveKVItemResponse(request.kvitem.kv_id, request.kvitem.key)

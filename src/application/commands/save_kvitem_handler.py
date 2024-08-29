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
        self.logger("request validated")
        # 2. business rule validation
        biz_validator = SaveKVItemBizValidator(self.repository, self.localizer)
        biz_validator.validate_and_throw(request)
        self.logger("business rules validated")

        self.repository.begin()
        if request.is_update:
            self.repository.kvitem.update(request.kvitem)
        else:
            self.repository.kvitem.create(request.kvitem)
        self.repository.commit_work()

        return SaveKVItemResponse(request.kvitem.kv_id, request.kvitem.key)

"""_summary_
    """
import logging
from toolkit import Localizer
from domain.ports import CoreRepository
from application.messages import SaveKVItemsRuleRequest, SaveKVItemsRuleResponse
from application.validators import SaveKVItemValidator, SaveKVItemBizValidator


class SaveKVItemsHandler:
    """ KV Item Handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer

    def handler(self, request: SaveKVItemsRuleRequest):
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
        if len(request.insert_kvitems) > 0:
            for it in request.insert_kvitems:
                self.repository.kvitem.update(it)
        if len(request.kvitems_to_insert) > 0:
            for it in request.kvitems_to_insert:
                self.repository.kvitem.create(it)
        self.repository.commit_work()

        return SaveKVItemsRuleResponse(request.kvitem.kv_id, request.kvitem.key)

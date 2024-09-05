"""_summary_
    """
import logging
from application.messages import SaveActionRequest, SaveActionResponse
from application.validators import SaveActionValidator, SaveActionBizValidator
from domain.ports import CoreRepository
from toolkit import Localizer


class SaveActionHandler:
    """ Save Action Handler """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer

    def handler(self, request: SaveActionRequest):
        """ Handler """
        # 1. request validation
        validator = SaveActionValidator(self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("request validated")
        # 2. business rules validation
        biz_validator = SaveActionBizValidator(self.localizer, self.repository)
        biz_validator.validate_and_throw(request)
        self.logger.info("business rules validated")

        self.repository.begin()
        if request.is_update:
            self.repository.action.update(request.action)
        else:
            self.repository.action.create(request.action)
        self.repository.commit_work()

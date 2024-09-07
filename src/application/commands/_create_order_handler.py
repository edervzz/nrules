""" Create Order Handler """
import logging
from domain.ports import CoreRepository
from toolkit import Localizer
from application.messages import CreateOrderResponse


class CreateOrderHandler:
    """ Create order """

    def __init__(self, repository: CoreRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer

    def handler(self):
        """ handler """

        return CreateOrderResponse(1)

""" services available in all app """

import os
import logging
from domain.ports import CoreRepository
from infrastructure.adapters import CoreAdapter, StubRepositoryAdapter
from toolkit import Localizer


class Services():
    """ Services container """
    tenant_id: int
    core_repository: CoreRepository
    logger: logging.Logger
    localizer: Localizer

    @classmethod
    def prepare(cls) -> None:
        """ prepare services """
        # repository
        try:
            __repository = CoreAdapter(
                os.environ["TENANT_DBUSER"],
                os.environ["TENANT_DBPWD"],
                os.environ["TENANT_DBSERVER"],
                os.environ["TENANT_DBNAME"]
            )
        except KeyError:
            __repository = StubRepositoryAdapter()
        Services.core_repository = __repository

        # logger
        logging.basicConfig()
        Services.logger = logging.getLogger(__name__)

        # localizer
        Services.localizer = Localizer()

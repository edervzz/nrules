""" services available in all app """

import os
import logging
from domain.ports import Repository
from infrastructure.adapters import RepositoryAdapter, StubRepositoryAdapter
from toolkit import Localizer


class Services():
    """ Services container """
    tenant_id: int
    repository: Repository
    logger: logging.Logger
    localizer: Localizer

    @classmethod
    def prepare(cls) -> None:
        """ prepare services """
        # repository
        try:
            __repository = RepositoryAdapter(
                os.environ["DBUSER"],
                os.environ["DBPWD"],
                os.environ["DBSERVER"],
                os.environ["DBNAME"]
            )
        except KeyError:
            __repository = StubRepositoryAdapter()
        Services.repository = __repository

        # logger
        logging.basicConfig()
        Services.logger = logging.getLogger(__name__)

        # localizer
        Services.localizer = Localizer()

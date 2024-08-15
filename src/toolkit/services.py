""" services available in all app """
import logging
import os
from domain.ports import Repository
from infrastructure.adapters import RepositoryAdapter, StubRepositoryAdapter


class Services():
    """ Services container """
    repository: Repository
    logger: logging.Logger

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

""" Dependency Injection """
import logging
import os
from infrastructure.adapters import RepositoryAdapter


def get_logger():
    """ retrieve logger transcient instance """
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    return logger


def get_repository():
    """ retrieve repository transcient instance """
    repository = RepositoryAdapter(
        os.environ["DBUSER"], os.environ["DBPWD"], os.environ["DBSERVER"], os.environ["DBNAME"])
    return repository

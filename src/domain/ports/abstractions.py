""" abstractions for reepository"""
from abc import abstractmethod
from sqlalchemy import Engine
from sqlalchemy.orm import Session


class Creator:
    """ creator repository """

    def __init__(self) -> None:
        self.session: Session  # <- for mutation purpose
        self.engine: Engine  # <- for query purpose

    @abstractmethod
    def set_session(self, session: Session):
        """ assign session from engine """
        self.session = session

    @abstractmethod
    def create(self, entity):
        """ create a new entity """
        raise NotImplementedError(__name__)


class Updater:
    """ creator repository """

    @abstractmethod
    def update(self, entity):
        """ update an entity """
        raise NotImplementedError(__name__)


class ReaderSingle:
    """ reader repository """

    @abstractmethod
    def read(self, _id) -> any:
        """ read entity by id """
        raise NotImplementedError(__name__)


class ReaderSingleByExternalID:
    """ reader single repository """

    @abstractmethod
    def read_by_external_id(self, external_id: str) -> any:
        """ read entity by external id """
        raise NotImplementedError(__name__)


class ReaderByParentID:
    """ reader many from parent """

    @abstractmethod
    def read_by_parent_id(self, parent_id: int) -> []:
        """ read entities by parent id """
        raise NotImplementedError(__name__)


class ReaderPagination:
    """ reader all using pagination """

    @abstractmethod
    def read_page(self, page_no: int, page_size: int) -> tuple[list, any]:
        """_summary_

        Args:
            page_no (int): Number of page
            page_size (int): Size of page

        Raises:
            NotImplementedError: _description_

        Returns:
            tuple[list, any]: return list of entites and data pagination
        """
        raise NotImplementedError(__name__)

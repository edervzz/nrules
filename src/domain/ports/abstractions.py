"""repositories"""
from sqlalchemy import Engine
from sqlalchemy.orm import Session


class MutationRepository:
    """ creator repository """

    def __init__(self) -> None:
        self.session: Session

    def set_session(self, session: Session):
        """ assign session from engine """
        self.session = session

    def create(self, entity):
        """ create a new entity """
        raise NotImplementedError(__name__)

    def update(self, entity):
        """ update an entity """
        raise NotImplementedError(__name__)


class QueryRepository:
    """ reader repository """

    def __init__(self) -> None:
        self.engine: Engine

    def read(self, tenantid: int, _id: int) -> any:
        """ read entity by id """
        raise NotImplementedError(__name__)

    def read_by_external_id(self, tenantid: int, external_id: str) -> any:
        """ read entity by external id """
        raise NotImplementedError(__name__)


class QueryFromParentRepository:
    """ reader from parent """

    def read_by_parent_id(self, tenantid: int, parent_id: int) -> []:
        """ read entities by parent id """
        raise NotImplementedError(__name__)


class QueryPaginationRepository:
    """ reader from parent """

    def read_page(self, tenantid: int, page_no: int, page_size: int) -> tuple[list, any]:
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

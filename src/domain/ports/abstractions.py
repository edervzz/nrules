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

    def read(self, _id: int) -> any:
        """ read entity by id """
        raise NotImplementedError(__name__)

    def read_by_external_id(self, external_id: str) -> any:
        """ read entity by external id """
        raise NotImplementedError(__name__)


class QueryFromParentRepository:
    """ reader from parent """

    def read_by_parent_id(self, parent_id: int) -> []:
        """ read entities by parent id """
        raise NotImplementedError(__name__)

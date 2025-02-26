""" core repositories """
from abc import ABC, abstractmethod
from .abstractions import Creator, Updater
from .abstractions import ReaderByParentID, ReaderPagination
from .abstractions import ReaderSingle, ReaderSingleByExternalID, ReaderByLink


class LockRepository(
        ABC, Creator, ReaderSingle):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine

    @abstractmethod
    def delete(self, _id):
        """ delete a entity """
        raise NotImplementedError(__name__)


class KVItemRepository(
        ABC, Creator, Updater, ReaderSingle, ReaderByParentID,
        ReaderByLink):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine


class RuleRepository(
        ABC, Creator, Updater,
        ReaderSingle, ReaderSingleByExternalID, ReaderPagination):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine

    @abstractmethod
    def read_page_by_short(self, page_no: int, page_size: int, short_id: str) -> tuple[list, any]:
        """ Read page by short ID """


class TagRepository(
        ABC, Creator, Updater,
        ReaderSingleByExternalID, ReaderByParentID):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine


class ParametersRepository(
        ABC, Creator, Updater,
        ReaderSingle, ReaderByParentID):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine


class ConditionRepository(
        ABC, Creator, Updater,
        ReaderSingle, ReaderByParentID, ReaderByLink):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine


class CaseRepository(
        ABC, Creator, Updater,
        ReaderSingle, ReaderByParentID):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine


class CoreRepository:
    """ Repository container """

    # "mysql+pymysql://root:my-secret-pw@localhost/nrule-core", echo=True)
    def __init__(self):
        self.rule: RuleRepository
        self.case: CaseRepository
        self.condition: ConditionRepository
        self.kvitem: KVItemRepository
        self.parameter: ParametersRepository
        self.tag: TagRepository

    @abstractmethod
    def begin(self, autoflush=False):
        """ Begin transaction """

    @abstractmethod
    def commit_work(self):
        """ Commit transaction """

    @abstractmethod
    def rollback_work(self):
        """ Rollback transaction """

    @abstractmethod
    def migrate(self) -> list:
        """ Run Migration """

    @abstractmethod
    def health_check(self) -> list:
        """ Run Migration """

    @abstractmethod
    def next_number(self, class_) -> str:
        """ Get next number """

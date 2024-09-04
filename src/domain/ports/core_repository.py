""" core repositories """
from abc import ABC, abstractmethod
from .abstractions import Creator, Updater
from .abstractions import ReaderByParentID, ReaderPagination, ReaderSingle, ReaderSingleByExternalID


class KVSRepository(ABC, Creator, ReaderSingle, ReaderSingleByExternalID):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine


class KVItemRepository(ABC, Creator, Updater, ReaderSingle, ReaderByParentID):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine


class ActionRepository(ABC, Creator, ReaderSingle):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine


class RuleRepository(
        ABC, Creator, Updater,
        ReaderSingle, ReaderByParentID, ReaderSingleByExternalID, ReaderPagination):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine


class WorkflowRepository(
        ABC, Creator, Updater,
        ReaderSingle, ReaderSingleByExternalID, ReaderPagination):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine


class ContainerRepository(ABC, Creator, Updater, ReaderByParentID):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine


class EntrypointRepository(ABC, Creator, ReaderSingle, ReaderSingleByExternalID):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine


class VariantRepository(ABC, Creator, Updater, ReaderByParentID):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine


class XObjectRepository(ABC, Creator):
    """_summary_"""

    def __init__(self, engine):
        ABC.__init__(self)
        Creator.__init__(self)
        self.engine = engine


class CoreRepository:
    """ Repository container """

    # "mysql+pymysql://root:my-secret-pw@localhost/nrule-core", echo=True)
    def __init__(self):
        self.kvs: KVSRepository
        self.kvitem: KVItemRepository
        self.action: ActionRepository
        self.rule: RuleRepository
        self.workflow: WorkflowRepository
        self.container: ContainerRepository
        self.entrypoint: EntrypointRepository
        self.variant: VariantRepository

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
    def next_number(self, class_) -> int:
        """ Get next number """

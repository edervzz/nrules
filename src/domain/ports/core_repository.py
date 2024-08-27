"""_summary_
    """
from abc import ABC
from domain.entities import Workflow
from .abstractions import Creator, Updater
from .abstractions import ReaderByParentID, ReaderPagination, ReaderSingle, ReaderSingleByExternalID


class KVSRepository(Creator, ReaderSingle):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class KVItemRepository(Creator, ReaderSingle):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class ActionRepository(Creator, ReaderSingle):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class RuleRepository(Creator, Updater, ReaderSingle, ReaderByParentID, ReaderSingleByExternalID, ReaderPagination):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class WorkflowRepository(Creator, Updater, ReaderSingle, ReaderSingleByExternalID):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class ContainerRepository(Creator, ReaderSingle):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class EntrypointRepository(Creator, ReaderSingle):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class VariantRepository(Creator, ReaderSingle):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class XObjectRepository(Creator):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class CoreRepository(ABC):
    """ Repository container """

    # "mysql+pymysql://root:my-secret-pw@localhost/nrule-core", echo=True)
    def __init__(self):
        self.rule: RuleRepository
        self.workflow: WorkflowRepository

    def create(self, entity: any):
        """ Create a new entity """

    def update(self, entity: any):
        """ Update an entity """

    def workflow_read(self, _id: int) -> Workflow:
        """ read an entity by id """

    def workflow_read_by_external_id(self, external_id: str) -> Workflow:
        """ read an entity by id """

    def begin(self, autoflush=False):
        """ Begin transaction """

    def commit_work(self):
        """ Commit transaction """

    def rollback_work(self):
        """ Rollback transaction """

    def migrate(self):
        """ Run Migration """

    def health_check(self) -> list:
        """ Run Migration """

    def next_number(self, class_) -> int:
        """ Get next number """

""" tenancy repository """
from abc import ABC, abstractmethod
from .abstractions import Creator, Updater, ReaderSingle, ReaderSingleByExternalID


class TenantRepository(ABC, Creator, ReaderSingle):
    """ Tenant repository """

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class TenantStageRepository(ABC, Creator, Updater, ReaderSingle, ReaderSingleByExternalID):
    """ Tenant stage repository """

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class TenancyRepository(ABC):
    """ Tenancy Repository container """

    # "mysql+pymysql://root:my-secret-pw@localhost/dbname", echo=True)
    def __init__(self):
        self.tenant: TenantRepository
        self.tenant_stage: TenantStageRepository

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
    def migrate(self):
        """ Run Migration """

    @abstractmethod
    def health_check(self) -> list:
        """ Run Migration """

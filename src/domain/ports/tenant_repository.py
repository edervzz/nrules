"""_summary_
    """
from abc import ABC
from .abstractions import MutationRepository, QueryRepository


class TenantRepository(MutationRepository, QueryRepository):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class TenantStageRepository(MutationRepository, QueryRepository):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class TenancyRepository(ABC):
    """ Repository container """

    # "mysql+pymysql://root:my-secret-pw@localhost/nrule-core", echo=True)
    def __init__(self):
        self.tenant: TenantRepository
        self.tenant_stage: TenantStageRepository

    def create(self, entity: any):
        """ Create a new entity """

    def update(self, entity: any):
        """ Update an entity """

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

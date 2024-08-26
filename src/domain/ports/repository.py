"""_summary_
    """
from abc import ABC
from domain.entities import Workflow
from .entity_repository import RuleRepository, WorkflowRepository, TenantRepository, TenantStageRepository


class Repository(ABC):
    """ Repository container """

    # "mysql+pymysql://root:my-secret-pw@localhost/nrule-core", echo=True)
    def __init__(self):
        self.tenant: TenantRepository
        self.tenant_stage: TenantStageRepository
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

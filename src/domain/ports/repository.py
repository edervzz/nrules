"""_summary_
    """
from abc import ABC
from typing import List
from domain.entities import Workflow, Rule


class Repository(ABC):
    """ Repository container """

    # "mysql+pymysql://root:my-secret-pw@localhost/nrule-core", echo=True)
    def __init__(self):
        pass

    def create(self, entity: any):
        """ Create a new entity """

    def update(self, entity: any):
        """ Update an entity """

    def workflow_read_by_external_id(self, external_id: str) -> Workflow:
        """ read an entity by id """

    def rules_read_by_parent_id(self, parent_id: int) -> List[Rule]:
        """ read rules by parent id """

    def begin(self):
        """ Begin transaction """

    def commit_work(self):
        """ Commit transaction """

    def rollback_work(self):
        """ Rollback transaction """

    def migrate(self):
        """ Run Migration """

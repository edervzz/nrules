"""_summary_
    """
from abc import ABC
from sqlalchemy.orm import Session
from toolkit import Writer, Updater


class WorkflowRepository(Writer):
    """ Workflow repository """


class RuleRepository(Writer, Updater):
    """ Rule repository """


class Repository(ABC):
    """ Repository container """
    __session__: Session
    workflowRepository: WorkflowRepository

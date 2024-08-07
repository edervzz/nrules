"""_summary_
    """
from typing import TypeVar
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

T = TypeVar("T")


class Repository(ABC):
    """ Repository container """

    def __init__(self):
        """ session (Session): used for sql transactions
            workflow_repository (WorkflowRepository): workflow entity-table
        """
        self.session: Session = None

    @abstractmethod
    def create(self, entity: T):
        """ Create a new entity """

    @abstractmethod
    def update(self, entity: T):
        """ Update an entity """

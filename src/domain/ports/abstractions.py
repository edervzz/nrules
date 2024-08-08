""" Abstractions """
from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")


class Writer(ABC):
    """ Writer """

    def create(self, entity: T):
        """ Create a new entity """


class Updater(ABC):
    """ Updated """

    def update(self, entity: T):
        """ Update an entity """

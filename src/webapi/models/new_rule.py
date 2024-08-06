""" Rule module """

from dataclasses import dataclass


@dataclass
class NewRule:
    """ New Rule request """
    name: str
    expression: str

""" Exceptions classes based on http exceptions """

from abc import ABC, abstractmethod
import json
from typing import List
from werkzeug.exceptions import Conflict, BadRequest, NotFound


class Validator(ABC):
    """ Raise when any format error is reached. """

    def __init__(self):
        self.__messages_codes: List[dict[str, str]] = []

    def validate_and_throw(self, request):
        """ Execute validations """
        self.__validate__(request)
        if len(self.__messages_codes) > 0:
            raise BadRequest(json.dumps(self.__messages_codes))

    def any_error(self) -> bool:
        """ return true when any error was collected """
        return len(self.__messages_codes) > 0

    def add_failure(self, code_message: tuple[str, str]):
        """ Add a message code into collection. """
        code, message = code_message
        self.__messages_codes.append({'code': code, 'message': message})

    def as_error(self, code_message: tuple[str, str]):
        """ Raise a single Validation Error """
        code, message = code_message
        self.__messages_codes.append({'code': code, 'message': message})
        return BadRequest(json.dumps(self.__messages_codes))

    def as_not_found(self, code_message: tuple[str, str]):
        """ Raise a single Not Found Error """
        code, message = code_message
        self.__messages_codes.append({'code': code, 'message': message})
        return NotFound(json.dumps(self.__messages_codes))

    def as_duplicated(self, code_message: tuple[str, str]):
        """ Raise a single  Duplicated Error """
        code, message = code_message
        self.__messages_codes.append({'code': code, 'message': message})
        return Conflict(json.dumps(self.__messages_codes))

    @ abstractmethod
    def __validate__(self, request):
        """ Validate request format

            Abstract method.
        """

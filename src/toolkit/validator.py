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

    def add_failure(self, code: str, message: str):
        """ Add a message code into collection. """
        self.__messages_codes.append({'code': code, 'message': message})

    def as_error(self, code: str, message: str):
        """ Raise a single Validation Error """
        return BadRequest(json.dumps({'code': code, 'message': message}))

    def as_not_found(self, code: str, message: str):
        """ Raise a single Not Found Error """
        return NotFound(json.dumps({'code': code, 'message': message}))

    def as_duplicated(self,  code: str, message: str):
        """ Raise a single  Duplicated Error """
        return Conflict(json.dumps({'code': code, 'message': message}))

    @abstractmethod
    def __validate__(self, request):
        """ Validate request format 

            Abstract method.
        """

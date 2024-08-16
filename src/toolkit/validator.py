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

    def __addcode__(self, code: str, message: str):
        """ Add a message code into collection. """
        self.__messages_codes.append({'code': code, 'message': message})

    def __error__(self, code: str, message: str):
        """ Raise a single Validation Error """
        raise BadRequest(json.dumps({'code': code, 'message': message}))

    def __not_found__(self, description: str):
        """ Raise a single Not Found Error """
        raise NotFound(description)

    def __duplicated__(self, description: str, fields=None):
        """ Raise a single  Duplicated Error """
        raise Conflict(description)

    @abstractmethod
    def __validate__(self, request):
        """ Validate request format 

            Abstract method.
        """

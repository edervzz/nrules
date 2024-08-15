""" Exceptions classes based on http exceptions """

from abc import ABC, abstractmethod
import json
from typing import List
from werkzeug.exceptions import Conflict, BadRequest, NotFound
from .messages import get_message


class CustomError(ABC):
    """ Raise when any format error is reached. """

    def __init__(self):
        self.__messages_codes: List[str] = []

    def validate_and_throw(self, request):
        """ Execute validations """
        self.__validate__(request)
        if len(self.__messages_codes) > 0:
            datas = []
            for code in self.__messages_codes:
                data = get_message(code)
                datas.append(data)
            raise ValidationError(json_string=json.dumps(datas))

    @abstractmethod
    def __validate__(self, request):
        """ Validate request format 

            Abstract method.
        """

    def __add_message_code__(self, description: str):
        """ Add a message code into collection. """
        self.__messages_codes.append(description)

    def __raise_error__(self, description: str):
        """ Raise a single Validation Error """
        raise ValidationError(description)

    def __raise_not_found__(self, description: str):
        """ Raise a single Not Found Error """
        raise NotFoundError(description)

    def __raise_duplicated__(self, description: str):
        """ Raise a single  Duplicated Error """
        raise DuplicatedError(description)


class DuplicatedError(Conflict):
    """ Raise when an object already exists in data store """

    def __init__(self, description: str | None = None) -> None:
        self.messages_codes: List[str] = []
        self.datas = []

        if description is not None:
            self.datas.append(get_message(description))
            json_str = json.dumps(self.datas)
            super().__init__(json_str)
        else:
            super().__init__("")


class NotFoundError(NotFound):
    """ Raise when an object don't exists in data store """

    def __init__(self, description: str | None = None) -> None:
        self.messages_codes: List[str] = []
        self.datas = []

        if description is not None:
            self.datas.append(get_message(description))
            json_str = json.dumps(self.datas)
            super().__init__(json_str)
        else:
            super().__init__("")


class ValidationError(BadRequest):
    """ Raise when any format error is reached. """

    def __init__(self, description: str | None = None, json_string: str | None = None):
        self.messages_codes: List[str] = []
        self.datas = []

        if description is not None:
            self.datas.append(get_message(description))
            json_str = json.dumps(self.datas)
            super().__init__(json_str)
        elif json_string is not None:
            super().__init__(json_string)
        else:
            super().__init__("")

    def add_message_code(self, description: str):
        """ Collect a message code. 

        _pass_or_raise()_ method requires to be called at end of validation. """

        self.messages_codes.append(description)

    def pass_or_raise(self):
        """ When at least one messages code exists into collection, raise a new ValidationError detailed. """

        if len(self.messages_codes) > 0:
            datas = []
            for code in self.messages_codes:
                data = get_message(code)
                datas.append(data)
            raise ValidationError(json_string=json.dumps(datas))

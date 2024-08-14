""" Exceptions classes """

import json
from typing import List
from werkzeug.exceptions import Conflict, BadRequest
from .messages import get_message


class DuplicatedError(Conflict):
    """ Object duplicated """

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
    """ Format Checks """

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
        """ Add a message code """
        self.messages_codes.append(description)

    def pass_or_raise(self):
        """ Check messages codes and raise a new ValidationError """
        if len(self.messages_codes) > 0:
            datas = []
            for code in self.messages_codes:
                data = get_message(code)
                datas.append(data)
            raise ValidationError(json_string=json.dumps(datas))

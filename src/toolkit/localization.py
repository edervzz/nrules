""" Message catalog """
from typing import List
from .messages import Codes


class Localizer:
    """ Localization class """

    def get(self, code: str, params: List[str] = None):
        """ retrieve message """
        if code in Codes.en_messages:
            mess = Codes.en_messages[code].format(
                *params) if params is not None else Codes.en_messages[code]
            return mess

        else:
            return code

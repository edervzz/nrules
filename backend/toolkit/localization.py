""" Message catalog """
from .messages import Codes


class Localizer:
    """ Localization class """

    def __init__(self):
        self.langu = "en"

    def get(self, code: str, *params):
        """ retrieve message """
        if self.langu == "es":
            mess = Codes.es_messages[code] if code in Codes.es_messages else code
        else:
            mess = Codes.en_messages[code] if code in Codes.en_messages else code

        if params is not None:
            mess = mess.format(*params)

        return (code, mess)

    def set_langu(self, langu: str):
        """ define langu for current request """
        self.langu = langu.upper()

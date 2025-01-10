""" _module_ """
from domain.entities import Parameter
from toolkit import Localizer, Codes, Validator, Constants


class ParameterValidator(Validator):
    """_summary_"""

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: Parameter):
        """ Validate request format """
        request.key = request.key.strip()
        request.usefor = request.usefor.upper().strip()
        request.typeof = request.typeof.upper().strip()

        if request.key == "" or request.usefor == "" or request.typeof == "":
            raise self.as_error(self._localizer.get(Codes.PARAM_001))

        if not (len(request.key) >= 5 and len(request.key) <= 50):
            raise self.as_error(self._localizer.get(Codes.PARAM_005))

        if request.usefor == Constants.INPUT:
            if not request.typeof in [Constants.STRING, Constants.NUMERIC, Constants.DATE]:
                raise self.as_error(self._localizer.get(
                    Codes.PARAM_003, request.key))
        elif request.usefor == Constants.OUTPUT:
            if not request.typeof in [Constants.JSON, Constants.STRING, Constants.NUMERIC, Constants.DATE]:
                raise self.as_error(self._localizer.get(
                    Codes.PARAM_004, request.key))
        else:
            raise self.as_error(self._localizer.get(
                Codes.PARAM_002, request.key))

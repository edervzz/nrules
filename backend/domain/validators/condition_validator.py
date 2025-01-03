"""_summary_"""
from domain.entities import Condition
from toolkit import Localizer, Codes, Validator, Constants


class ConditionValidator(Validator):
    """_summary_"""

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: Condition):
        """ Validate request format """

        if request.variable == "":
            self.add_failure(self._localizer.get(Codes.COND_001))

        if request.operator == "":
            self.add_failure(self._localizer.get(Codes.COND_002))

        if not request.typeof in [Constants.STRING, Constants.NUMERIC, Constants.DATE]:
            self.add_failure(self._localizer.get(Codes.COND_003))

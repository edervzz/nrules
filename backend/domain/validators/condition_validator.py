"""_summary_"""

from datetime import date
from domain.entities import Condition
from toolkit import Codes
from toolkit import Localizer, Validator


class ConditionValidator(Validator):
    """_summary_"""

    def __init__(self, localizer: Localizer, force_conv: bool):
        super().__init__()
        self.loc = localizer
        self.force_conv = force_conv

    def __validate__(self, request: Condition):
        """ Validate request format """

        c_date = "DATE"
        c_numeric = "NUMERIC"
        request.typeof = request.typeof.upper().strip()

        if request.typeof == c_numeric:
            try:
                request.value = str(float(request.value))
            except ValueError:
                if not self.force_conv:
                    request.value = ""
                else:
                    self.add_failure(
                        self.loc.get(Codes.COND_001, c_numeric))
                    return

        if request.typeof == c_date:
            dte = request.value.split("-")
            if len(dte) != 3:
                return
            try:
                request.value = str(date(dte[0], dte[1], dte[2]))
            except ValueError:
                if not self.force_conv:
                    request.value = ""
                else:
                    self.add_failure(
                        self.loc.get(Codes.COND_001, c_date))
                    return

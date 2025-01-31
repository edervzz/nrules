""" _module_ """
from datetime import date
from domain.entities import Condition
from toolkit import Localizer, Codes, Validator, Constants


class ConditionValidator(Validator):
    """ Validate Condition

        force_conv: when True raise a exception if conversion cannot be performed
    """

    def __init__(self, localizer: Localizer, force_conv: bool):
        super().__init__()
        self.loc = localizer
        self.force_conv = force_conv

    def __validate__(self, request: Condition):
        """ Validate request format """

        if request.variable == "":
            self.add_failure(self.loc.get(Codes.COND_001))

        if request.operator == "":
            self.add_failure(self.loc.get(Codes.COND_002))

        # if self.force_conv:
        #     if request.typeof == Constants.NUMERIC:
        #         try:
        #             request.value = str(float(request.value))
        #         except ValueError:
        #             self.add_failure(
        #                 self.loc.get(Codes.COND_004, request.value, Constants.NUMERIC))

        #     if request.typeof == Constants.DATE:
        #         dte = request.value.split("-")
        #         if len(dte) != 3:
        #             self.add_failure(self.loc.get(
        #                 Codes.COND_004, request.value, Constants.DATE))
        #             return
        #         try:
        #             request.value = str(date(dte[0], dte[1], dte[2]))
        #         except TypeError:
        #             self.add_failure(
        #                 self.loc.get(Codes.COND_004, request.value, Constants.DATE))

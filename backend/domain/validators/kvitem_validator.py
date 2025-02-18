""" _module_ """

from domain.entities import KVItem
from toolkit import Codes, Localizer, Validator


class KVItemValidator(Validator):
    """ Validate KV Item

        force_conv: when True raise a exception if conversion cannot be performed
    """

    def __init__(self, localizer: Localizer, force_conv: bool):
        super().__init__()
        self.loc = localizer
        self.force_conv = force_conv

    def __validate__(self, request: KVItem):
        """ Validate request format """
        request.key = request.key.upper().strip()
        request.value = request.value.upper().strip()

        if len(request.key) == 0:
            self.add_failure(self.loc.get(Codes.KVI_002))
        if len(request.case_id) == 0:
            self.add_failure(self.loc.get(Codes.KVI_006))
        if len(request.key) < 5 or len(request.key) > 50:
            self.add_failure(self.loc.get(Codes.KVI_003))
        if len(request.value) <= 500:
            self.add_failure(self.loc.get(Codes.KVI_004))

        request.calculation = "MOD" if request.calculation is None else request.calculation

        # if self.force_conv:
        #     if request.typeof == Constants.JSON:
        #         try:
        #             json.loads(request.value)
        #         except ValueError:
        #             self.add_failure(
        #                 self.loc.get(Codes.KVI_001, request.value, Constants.JSON))

        #     if request.typeof == Constants.NUMERIC:
        #         try:
        #             request.value = str(float(request.value))
        #         except ValueError:
        #             self.add_failure(
        #                 self.loc.get(Codes.KVI_001, request.value, Constants.NUMERIC))

        #     if request.typeof == Constants.DATE:
        #         dte = request.value.split("-")
        #         if len(dte) != 3:
        #             self.add_failure(self.loc.get(
        #                 Codes.KVI_001, request.value, Constants.DATE))
        #             return
        #         try:
        #             request.value = str(date(dte[0], dte[1], dte[2]))
        #         except TypeError:
        #             self.add_failure(
        #                 self.loc.get(Codes.KVI_001, request.value, Constants.DATE))

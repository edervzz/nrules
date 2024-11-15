"""_summary_"""
from typing import List
from domain.entities import Parameter
from application.messages import SaveConditionParamsRequest
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class SaveConditionsParamsValidator(Validator):
    """_summary_ """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: SaveConditionParamsRequest):
        """ Validate request format """

        if request.rule.id == 0 and request.rule.name == "":
            raise self.as_error(self._localizer.get(Codes.PARAM_UPD_002))

        totalparams: List[str] = []
        unique_cond_upsert: set[str] = {}
        any_change = False

        if isinstance(request.param_cond_upsert, list):
            unique_cond_upsert = duplicate_validator(
                request.param_cond_upsert, self, self._localizer)
            if len(unique_cond_upsert) > 0:
                any_change = True
            totalparams = list(unique_cond_upsert)

        unique_total = {x for x in totalparams}
        if len(unique_total) != len(unique_cond_upsert):
            self.add_failure(self._localizer.get(Codes.PARAM_UPD_004))

        if not any_change:
            self.add_failure(self._localizer.get(Codes.OBJ_UPD_001))


def duplicate_validator(params: List[Parameter], v: Validator, local: Localizer):
    """ duplicate_validator """
    if isinstance(params, list):
        r: List[str] = []
        if params.count > 0:
            unique = {x.key for x in params}
            if len(unique) != len(params):
                v.add_failure(local.get(Codes.PARAM_UPD_003))
                return r
            return list(unique)

    return r

""" _module_ """
from toolkit import Validator, Localizer, Codes, Constants
from application.messages import UpdateKVItemsRuleRequest
from domain.entities import Parameter
from domain.validators import ParameterValidator, KVItemValidator


class UpdateKVItemsRuleValidator(Validator):
    """_summary_"""

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.localizer = localizer

    def __validate__(self, request: UpdateKVItemsRuleRequest):
        """ validate """
        if request.id == "" and request.name == "":
            self.as_error(self.localizer.get(Codes.KVI_UPD_001))

        if len(request.income_kvitems) == 0:
            self.as_error(self.localizer.get(Codes.KVI_UPD_002))

        unique_items = set()
        validator_kvi = KVItemValidator(self.localizer, False)
        validator_param = ParameterValidator(self.localizer)

        if not request.income_kvitems is None:
            for new_kvitem in request.income_kvitems:
                new_kvitem.key = new_kvitem.key.upper()
                # validate condition
                validator_kvi.validate_and_throw(new_kvitem)
                # prepare parameter
                param = Parameter()
                param.key = new_kvitem.key
                param.usefor = Constants.OUTPUT
                param.typeof = new_kvitem.typeof
                param.is_active = new_kvitem.is_active
                param.is_archived = new_kvitem.is_archived
                # validate parameter
                validator_param.validate_and_throw(param)
                # collect parameter
                request.upd_parameters.append(param)
                unique_items.add(param.key)

        if len(unique_items) != len(request.upd_parameters):
            raise self.as_error(self.localizer.get(Codes.KVI_CREA_003))

        if len(request.upd_parameters) != len(request.income_kvitems):
            raise self.as_error(self.localizer.get(Codes.KVI_CREA_004))

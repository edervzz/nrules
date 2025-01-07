"""_summary_
    """
from toolkit import Localizer, Validator, Codes, Constants
from application.messages import SaveKVItemsRuleRequest
from domain.entities import Parameter
from domain.validators import KVItemValidator, ParameterValidator


class SaveKVItemValidator(Validator):
    """ Create KV Item Validator """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.localizer = localizer

    def __validate__(self, request: SaveKVItemsRuleRequest):
        validator_kvitem = KVItemValidator(self.localizer, False)
        validator_param = ParameterValidator(self.localizer)

        unique_items = set()

        if len(request.insert_kvitems) > 0:
            for kvit in request.insert_kvitems:
                # validate kv item
                validator_kvitem.validate_and_throw(kvit)
                # prepare parameter
                param = Parameter()
                param.key = kvit.key
                param.usefor = Constants.OUTPUT
                param.typeof = kvit.typeof
                # validate parameter
                validator_param.validate_and_throw(param)
                # collect parameter
                request.insert_parameters.append(param)
                unique_items.add(param.key)

        if len(request.update_kvitems) > 0:
            for kvit in request.insert_kvitems:
                # validate kv item
                validator_kvitem.validate_and_throw(kvit)
                # prepare parameter
                param = Parameter()
                param.key = kvit.key
                param.usefor = Constants.OUTPUT
                param.typeof = kvit.typeof
                # validate parameter
                validator_param.validate_and_throw(param)
                # collect parameter
                request.update_parameters.append(param)
                unique_items.add(param.key)

        if len(unique_items) != (len(request.update_parameters) + len(request.insert_parameters)):
            raise self.as_error(self.localizer.get(Codes.KVI_SAVE_001))

        if len(request.update_parameters) != len(request.update_kvitems):
            raise self.as_error(self.localizer.get(Codes.KVI_SAVE_002))

        if len(request.insert_parameters) != len(request.insert_kvitems):
            raise self.as_error(self.localizer.get(Codes.KVI_SAVE_002))

""" _module_ """
from toolkit import Validator, Localizer, Codes
from application.messages import UpdateKVItemsRuleRequest
from domain.validators import KVItemValidator


class UpdateKVItemsRuleValidator(Validator):
    """_summary_"""

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.localizer = localizer

    def __validate__(self, request: UpdateKVItemsRuleRequest):
        """ validate """
        if request.id == "" and request.name == "":
            raise self.as_error(self.localizer.get(Codes.KVI_UPD_001))

        if len(request.income_kvitems) == 0:
            raise self.as_error(self.localizer.get(Codes.KVI_UPD_002))

        unique_items = set()
        validator_kvi = KVItemValidator(self.localizer, False)

        if not request.income_kvitems is None:
            for kvi in request.income_kvitems:
                kvi.key = kvi.key.lower()
                # validate condition
                validator_kvi.validate_and_throw(kvi)
                unique_items.add(kvi.key)

        if len(unique_items) != len(request.income_kvitems):
            raise self.as_error(self.localizer.get(Codes.KVI_UPD_003))

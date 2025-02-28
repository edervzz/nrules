"""_summary_"""
from toolkit import Validator, Localizer, Codes
from application.messages import UpdateParametersRuleRequest
from domain.validators import ParameterValidator


class UpdateParametersRuleValidator(Validator):
    """_summary_"""

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.localizer = localizer

    def __validate__(self, request: UpdateParametersRuleRequest):
        """ validate """
        if request.id == "" and request.name == "":
            raise self.as_error(self.localizer.get(Codes.PARAM_UPD_001))

        if len(request.parameters) == 0:
            raise self.as_error(self.localizer.get(Codes.PARAM_UPD_002))

        unique_items = set()
        validator_param = ParameterValidator(self.localizer)

        if not request.parameters is None:
            for upd_param in request.parameters:
                upd_param.key = upd_param.key.lower()
                # validate parameter
                validator_param.validate_and_throw(upd_param)
                unique_items.add(f"{upd_param.key}{upd_param.usefor}")

        if len(unique_items) != len(request.parameters):
            raise self.as_error(self.localizer.get(Codes.PARAM_UPD_003))

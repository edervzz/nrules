"""_summary_
    """
from toolkit import Validator, Localizer, Codes
from application.messages import SaveRuleConditionsRequest


class SaveRuleConditionsValidator(Validator):
    """_summary_"""

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.localizer = localizer

    def __validate__(self, request: SaveRuleConditionsRequest):
        """ validate """
        if request.id == "" and request.name == "":
            self.as_error(self.localizer.get(Codes.COND_SAVE_007))

        if request.upsert_conditions.count > 0:
            for c in request.upsert_conditions:
                if c.variable == "":
                    raise self.as_error(
                        self.localizer.get(Codes.COND_SAVE_001))
                if not c.typeof in ["STRING", "NUMERIC", "DATE"]:
                    raise self.as_error(
                        self.localizer.get(Codes.COND_SAVE_002))
                if not c.operator in ["=", "<>", ">", "<", ">=", "<=", "IN", "NI", "BT", "NB"]:
                    raise self.as_error(
                        self.localizer.get(Codes.COND_SAVE_003))

                match c.typeof:
                    case "STRING":
                        if not c.operator in ["=", "<>", "IN", "NI"]:
                            raise self.as_error(
                                self.localizer.get(Codes.COND_SAVE_004))
                    case "NUMERIC":
                        if not c.operator in ["=", "<>", ">", "<", ">=", "<=", "IN", "NI", "BT", "NB"]:
                            raise self.as_error(
                                self.localizer.get(Codes.COND_SAVE_005))
                    case "DATE":
                        if not c.operator in ["=", "<>", ">", "<", ">=", "<=", "BT", "NB"]:
                            raise self.as_error(
                                self.localizer.get(Codes.COND_SAVE_006))

        if request.delete_conditions.count > 0:
            pass

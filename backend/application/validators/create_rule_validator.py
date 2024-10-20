"""_summary_"""
from application.messages import CreateRuleRequest
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class CreateRuleValidator(Validator):
    """_summary_ """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: CreateRuleRequest):
        """ Validate request format """

        if request.rule.name == "":
            self.add_failure(self._localizer.get(Codes.RU_CREA_001))

        if request.rule.rule_type is None:
            self.add_failure(self._localizer.get(Codes.RU_CREA_008))
        else:
            if request.rule.rule_type.upper() not in ["MATRIX", "TREE"]:
                self.add_failure(self._localizer.get(Codes.RU_CREA_004))
            if request.rule.rule_type.upper() == "MATRIX":
                if request.rule.strategy not in ["EARLY", "BASE", "ALL"]:
                    self.add_failure(self._localizer.get(Codes.RU_CREA_011))

        if len(request.rule.name) < 5 or len(request.rule.name) > 50:
            self.add_failure(self._localizer.get(Codes.RU_CREA_002))
        else:
            unique = set()
            error_field = False
            for c in request.paramters:
                c.key = c.key.strip()
                c.usefor = c.usefor.strip()
                c.typeof = c.typeof.strip()
                c.rule_id = request.rule.id
                unique.add(c.key)

                if c.key == "" or c.usefor == "" or c.typeof == "":
                    self.add_failure(self._localizer.get(Codes.RU_CREA_012))
                    error_field = True
                    break

            if not error_field:
                if len(unique) != len(request.paramters):
                    self.add_failure(self._localizer.get(Codes.RU_CREA_013))

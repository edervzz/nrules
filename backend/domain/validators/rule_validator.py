""" _module_ """
from domain.entities import Rule
from toolkit import Localizer, Codes, Validator, Constants


class RuleValidator(Validator):
    """_summary_"""

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: Rule):
        """ Validate request format """
        request.name = request.name.lower()
        request.rule_type = request.rule_type.upper()
        request.strategy = request.strategy.upper()

        if request.name == "":
            self.add_failure(self._localizer.get(Codes.RULE_001))

        if len(request.name) < 5 or len(request.name) > 50:
            self.add_failure(self._localizer.get(Codes.RULE_005))

        if request.rule_type is None:
            self.add_failure(self._localizer.get(Codes.RULE_002))
        else:
            if request.rule_type not in [Constants.TABLE, Constants.TREE]:
                self.add_failure(self._localizer.get(Codes.RULE_003))
            if request.rule_type == Constants.TABLE:
                if request.strategy not in [Constants.EARLY, Constants.BASE, Constants.ALL]:
                    self.add_failure(self._localizer.get(Codes.RULE_004))

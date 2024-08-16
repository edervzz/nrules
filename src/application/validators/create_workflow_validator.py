"""_summary_"""
from application.messages import CreateWorkflowRequest
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class CreateWorkflowValidator(Validator):
    """_summary_ """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: CreateWorkflowRequest):
        """ Validate request format """

        if request.name == "":
            raise self.as_error(
                Codes.WF_CREA_001,
                self._localizer.get(Codes.WF_CREA_001))

        if len(request.name) < 5 or len(request.name) > 50:
            self.add_failure(
                Codes.WF_CREA_002,
                self._localizer.get(Codes.WF_CREA_002))

        if len(request.rules) == 0:
            self.add_failure(
                Codes.WF_CREA_004,
                self._localizer.get(Codes.WF_CREA_004))

        rule_names = []
        if len(request.rules) > 0:
            idx = 0
            for r in request.rules:
                idx += 1
                if r.name == "" or r.expression == "":
                    self.add_failure(
                        Codes.WF_CREA_005,
                        self._localizer.get(Codes.WF_CREA_005))
                if len(r.name) < 5 or len(r.name) > 50:
                    self.add_failure(
                        Codes.WF_CREA_007,
                        self._localizer.get(Codes.WF_CREA_007))
                if r.operator != "":
                    if r.operator != "AND" or r.operator != "OR":
                        self.add_failure(
                            Codes.WF_CREA_006,
                            self._localizer.get(Codes.WF_CREA_006))
                else:
                    r.operator = "AND"
                r.order = idx
                r.is_exclusive = False
                rule_names.append(r.name)

        rule_name_set = set(rule_names)
        if len(rule_name_set) != len(rule_names):
            self.add_failure(
                Codes.WF_CREA_008,
                self._localizer.get(Codes.WF_CREA_008))

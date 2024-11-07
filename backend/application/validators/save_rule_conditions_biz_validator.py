"""_summary_
    """
from application.messages import SaveRuleConditionsRequest
from domain.entities import Rule, Parameter
from domain.ports import CoreRepository
from toolkit import Validator, Localizer, Codes


class SaveRuleConditionsBizValidator(Validator):
    """_summary_"""

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repository = repository
        self.localizer = localizer

    def __validate__(self, request: SaveRuleConditionsRequest):
        """ validate """
        rule = None
        if request.id != "":
            rule = self.repository.rule.read(
                request.id)
        elif request.name != "":
            rule = self.repository.rule.read_by_external_id(
                request.name)
        if rule is None:
            raise self.as_not_found(self.localizer.get(Codes.COND_SAVE_008))

        rule_id = 0
        if isinstance(rule, Rule):
            rule_id = rule.id

        parameters = self.repository.parameter.read_by_parent_id(rule_id)
        if parameters is None:
            raise self.as_error(
                self.localizer.get(Codes.COND_SAVE_009))

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

                is_found = False
                for p in parameters:
                    if isinstance(p, Parameter):
                        if p.key == c.variable:
                            is_found = True
                            if p.usefor == "CONDITION":
                                p.typeof = c.typeof
                                request.update_parameter.append(p)
                                request.update_conditions.append(c)
                            else:
                                self.add_failure(
                                    self.localizer.get(Codes.COND_SAVE_010, c.variable))
                            break

                if not is_found:
                    p = Parameter()
                    p.key = c.variable
                    p.rule_id = rule_id
                    p.typeof = c.typeof
                    p.usefor = "CONDITION"

                    request.insert_parameters.append(p)
                    request.insert_conditions.append(c)

        if request.delete_conditions.count > 0:
            pass

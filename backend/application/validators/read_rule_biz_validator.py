""" _module_  """
from application.messages import ReadRuleRequest
from domain.ports import CoreRepository
from domain.entities import Rule, Case
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class ReadRuleBizValidator(Validator):
    """ Create Rule Validator """

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.__repository = repository
        self._localizer = localizer

    def __validate__(self, request: ReadRuleRequest):
        """ Validate request format """
        if request.rule_id != "":
            request.rule = self.__repository.rule.read(
                request.rule_id)
        elif request.rule_name != "":
            request.rule = self.__repository.rule.read_by_external_id(
                request.rule_name)

        if request.rule is None:
            raise self.as_not_found(self._localizer.get(Codes.RU_READ_002))

        if isinstance(request.rule, Rule) and request.full:
            request.parameters = self.__repository.parameter.read_by_parent_id(
                request.rule.id)
            cases = self.__repository.case.read_by_parent_id(request.rule.id)
            request.cases = cases
            if isinstance(cases, list):
                for case in cases:
                    if isinstance(case, Case):
                        conditions = self.__repository.condition.read_by_parent_id(
                            case.id)
                        request.conditions = request.conditions + conditions
                        kvitems = self.__repository.kvitem.read_by_parent_id(
                            case.id)
                        request.kvs_items = request.kvs_items + kvitems

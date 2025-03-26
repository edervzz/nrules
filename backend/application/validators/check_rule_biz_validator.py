import datetime
from typing import List
from toolkit import Validator, Localizer, Codes, Constants
from application.messages import CheckRuleRequest
from domain.entities import Rule, KVItem, Case, Condition, Parameter, RunRuleResult
from domain.ports import CoreRepository
from .expression_validator import ExpressionValidator


class CheckRuleBizValidator(Validator):
    """ validator """

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.localizer = localizer
        self.repo = repository

    def __validate__(self, request: CheckRuleRequest):
        request.rule = None
        if request.rule_id != "":
            request.rule = self.repo.rule.read(request.id)
        elif request.rule_name != "":
            request.rule = self.repo.rule.read_by_external_id(
                request.rule_name)
        if request.rule is None:
            raise self.as_not_found(self.localizer.get(Codes.RU_READ_002))

        formatdate = '%Y/%m/%d'

        parameters: List[Parameter] = self.repo.parameter.read_by_parent_id(
            request.rule.id)
        conditions: List[Condition] = self.repo.condition.read_by_link(
            request.rule.id)
        kvitems: List[KVItem] = self.repo.kvitem.read_by_link(request.rule.id)
        cases: List[Case] = self.repo.case.read_by_parent_id(request.rule.id)

        if not isinstance(parameters, list):
            raise self.as_error(self.localizer.get(Codes.CHK_RULE_001))
        if not isinstance(conditions, list):
            raise self.as_error(self.localizer.get(Codes.CHK_RULE_001))
        if not isinstance(kvitems, list):
            raise self.as_error(self.localizer.get(Codes.CHK_RULE_001))

        for ip in parameters:
            if ip.usefor == Constants.INPUT:
                myconditions = [x for x in conditions if x.variable == ip.key]
                match ip.typeof:
                    case Constants.STRING:
                        pass
                    case Constants.NUMERIC:
                        for cond in myconditions:
                            if not cond.value.isnumeric():
                                mycase = [x for x in cases if x.id ==
                                          cond.case_id][0]
                                if mycase.position < 9999:
                                    self.add_failure(self.localizer.get(
                                        Codes.CHK_RULE_002,
                                        f"{mycase.position}.{cond.operator}.{cond.value}",
                                        f"{ip.typeof}"))
                    case Constants.DATE:
                        for cond in myconditions:
                            myc = [x for x in cases if x.id == cond.case_id][0]
                            try:
                                if myc.position < 9999:
                                    datetime.datetime.strptime(
                                        cond.value, formatdate)
                            except ValueError:
                                self.add_failure(self.localizer.get(
                                    Codes.CHK_RULE_002,
                                    f"{mycase.position}.{cond.operator}.{cond.value}",
                                    f"{ip.typeof}"))

            if ip.usefor == Constants.OUTPUT:
                mykvis = [x for x in kvitems if isinstance(
                    x, KVItem) and x.key == ip.key]
                match ip.typeof:
                    case Constants.STRING:
                        pass
                    case Constants.NUMERIC:
                        for k in mykvis:
                            if not k.value.isnumeric():
                                mycase = [x for x in cases if isinstance(
                                    x, Case) and x.id == k.case_id][0]
                                self.add_failure(self.localizer.get(
                                    Codes.CHK_RULE_002,
                                    f"{mycase.position}.{k.value}",
                                    f"{ip.typeof}"))
                    case Constants.DATE:
                        for k in mykvis:
                            try:
                                datetime.datetime.strptime(
                                    k.value, formatdate)
                            except ValueError:
                                self.add_failure(self.localizer.get(
                                    Codes.CHK_RULE_002,
                                    f"{mycase.position}.{k.value}",
                                    f"{ip.typeof}"))

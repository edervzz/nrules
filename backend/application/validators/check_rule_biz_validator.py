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
            request.rule = self.repo.rule.read(request.rule_id)
        elif request.rule_name != "":
            request.rule = self.repo.rule.read_by_external_id(
                request.rule_name)
        if request.rule is None:
            raise self.as_not_found(self.localizer.get(Codes.RU_READ_002))

        formatdate = '%Y/%m/%d'

        myparameters: List[Parameter] = self.repo.parameter.read_by_parent_id(
            request.rule.id)
        myconditions: List[Condition] = self.repo.condition.read_by_link(
            request.rule.id)
        mykvitems: List[KVItem] = self.repo.kvitem.read_by_link(
            request.rule.id)
        mycases: List[Case] = self.repo.case.read_by_parent_id(request.rule.id)

        if not isinstance(myparameters, list):
            raise self.as_error(self.localizer.get(Codes.CHK_RULE_001))
        if not isinstance(myconditions, list):
            raise self.as_error(self.localizer.get(Codes.CHK_RULE_001))
        if not isinstance(mykvitems, list):
            raise self.as_error(self.localizer.get(Codes.CHK_RULE_001))
        if not isinstance(mycases, list):
            raise self.as_error(self.localizer.get(Codes.CHK_RULE_001))

        for a_cond in myconditions:
            theparam = [
                p for p in myparameters if p.key == a_cond.variable and p.usefor == Constants.INPUT][0]

            match theparam.typeof:
                case Constants.NUMERIC:
                    if not a_cond.value.isnumeric():
                        thecase = [
                            c for c in mycases if c.id == a_cond.case_id and c.position < 9999]
                        if len(thecase) > 0:
                            self.add_failure(self.localizer.get(
                                Codes.CHK_RULE_002,
                                f"{thecase[0].position}",
                                f"{a_cond.variable} {a_cond.operator} {a_cond.value}",
                                f"{theparam.typeof}"))

                case Constants.DATE:
                    try:
                        datetime.datetime.strptime(a_cond.value, formatdate)
                    except ValueError:
                        thecase = [
                            c for c in mycases if c.id == a_cond.case_id and c.position < 9999]
                        if len(thecase) > 0:
                            self.add_failure(self.localizer.get(
                                Codes.CHK_RULE_002,
                                f"{thecase[0].position}",
                                f"{a_cond.variable} {a_cond.operator} {a_cond.value}",
                                f"{theparam.typeof}"))

        for a_kvi in mykvitems:
            theparam = [
                p for p in myparameters if p.key == a_kvi.key and p.usefor == Constants.OUTPUT][0]

            match theparam.typeof:
                case Constants.NUMERIC:
                    if not a_kvi.value.isnumeric():
                        thecase = [
                            c for c in mycases if c.id == a_kvi.case_id and c.position < 9999][0]
                        self.add_failure(self.localizer.get(
                            Codes.CHK_RULE_003,
                            f"{thecase.position}",
                            f"{a_kvi.key}={a_kvi.value}",
                            f"{theparam.typeof}"))

                case Constants.DATE:
                    try:
                        datetime.datetime.strptime(a_kvi.value, formatdate)
                    except ValueError:
                        thecase = [
                            c for c in mycases if c.id == a_kvi.case_id and c.position < 9999][0]
                        self.add_failure(self.localizer.get(
                            Codes.CHK_RULE_003,
                            f"{thecase.position}",
                            f"{a_kvi.key}={a_kvi.value}",
                            f"{theparam.typeof}"))

""" summary """
from typing import List
from toolkit import Validator, Localizer, Codes
from application.messages import RunRuleRequest
from application.validators import ExpressionValidator
from domain.entities import Rule, KVItem, Condition
from domain.ports import CoreRepository


class RunRuleBizValidator(Validator):
    """ validator """

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self._local = localizer
        self._repo = repository

    def __validate__(self, request: RunRuleRequest):
        rule: Rule
        rule = self._repo.rule.read(
            request.rule_id) if request.rule_id != 0 else self._repo.rule.read_by_external_id(request.rule_name)

        if rule is None:
            self.add_failure(
                Codes.RUNNER_004,
                self._local.get(
                    Codes.RUNNER_004, request.kvs_id)
            )
            return

        conditions: List[Condition] = self._repo.condition.read_by_parent_id(
            rule.id)
        if conditions is None:
            request.ok = True  # by default, non conditions => truthy
            return

        kvitems: List[KVItem] = []
        if request.kvs_id != 0:
            kvitems = self._repo.kvitem.read_by_parent_id(request.kvs_id)
            if kvitems is None:
                self.add_failure(
                    Codes.RUNNER_003,
                    self._local.get(
                        Codes.RUNNER_003, request.rule_id if request.rule_id != 0 else request.rule_name)
                )
                return

        if self.any_error():
            return

        for cx in conditions:
            validator = ExpressionValidator(self._local)
            validator.validate_and_throw(cx)

            components, _ = validator.get_components_operators()
            # expression_results: List[bool] = []

            for cx in components:
                if cx.variable in request.payload:
                    value = request.payload[cx.variable]
                else:
                    self.add_failure(
                        Codes.RUNNER_002,
                        self._local.get(Codes.RUNNER_002, cx.variable,
                                        cx.variable+cx.operator+cx.value)
                    )
                    return

                passed = False
                match cx.operator:
                    case "EQ":
                        passed = value == cx.value
                    case "NE":
                        passed = value != cx.value
                    case "GT":
                        passed = value > cx.value
                    case "GE":
                        passed = value >= cx.value
                    case "LT":
                        passed = value < cx.value
                    case "LE":
                        passed = value <= cx.value
                    case "IN":
                        passed = value in cx.value

                if passed:
                    request.ok = True
                    request.kvitems = kvitems

                # expression_results.append(passed)

                # if len(expression_results) == 1:
                #     request.ok = expression_results[0]
                # else:
                #     r0 = expression_results[0]
                #     expression_results = expression_results[1:]
                #     idx = 0
                #     for rx in expression_results:
                #         op = operators[idx]
                #         if op == "<&&>":
                #             r0 = r0 and rx
                #         elif op == "<||>":
                #             r0 = r0 or rx

                #         idx += 1

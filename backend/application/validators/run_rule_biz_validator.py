""" summary """
from decimal import Decimal
from typing import List
from toolkit import Validator, Localizer, Codes
from application.messages import RunRuleRequest
from domain.entities import Rule, KVItem, Case, Condition, RunRuleResult
from domain.ports import CoreRepository
from .expression_validator import ExpressionValidator


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
            self.add_failure(self._local.get(Codes.RUNNER_003, request.rule_id)
                             )
            return

        request.trace.append(f"rule: {rule.name}, type:{rule.rule_type}")

        conditions: List[Case] = self._repo.case.read_by_parent_id(
            rule.id)
        if conditions is None:
            request.ok = True  # by default, non conditions => truthy
            return

        kvitems_input: List[KVItem] = []
        if request.kvs_id != 0:
            kvitems_input = self._repo.kvitem.read_by_parent_id(request.kvs_id)
            if kvitems_input is None:
                self.add_failure(self._local.get(Codes.RUNNER_003, request.rule_id if request.rule_id != 0 else request.rule_name)
                                 )
                return

        if self.any_error():
            return

        condition_ok = False
        for cit in conditions:
            expressions: List[Condition] = self._repo.condition.read_by_parent_id(
                cit.id)

            expression_results: List[bool] = []
            for exp in expressions:
                validator = ExpressionValidator(self._local)
                validator.validate_and_throw(exp.expression)

                components, operators = validator.get_components_operators()

                component_results: List[bool] = []
                for cx in components:
                    if cx.variable in request.payload:
                        value = request.payload[cx.variable]
                    else:
                        self.add_failure(self._local.get(
                            Codes.RUNNER_002, cx.variable))
                        return

                    passed = False
                    if cx.value == "<ANYVALUE>":
                        passed = True
                    else:
                        match cx.operator:
                            case "<EQ>":
                                passed = value == cx.value
                            case "<NE>":
                                passed = value != Decimal(cx.value)
                            case "<GT>":
                                passed = value > Decimal(cx.value)
                            case "<GE>":
                                passed = value >= Decimal(cx.value)
                            case "<LT>":
                                passed = value < Decimal(cx.value)
                            case "<LE>":
                                passed = value <= Decimal(cx.value)
                            case "<IN>":
                                passed = value in cx.value
                    component_results.append(passed)

                if len(component_results) == 1:
                    component_ok = component_results[0]
                else:
                    component_ok = component_results[0]
                    component_results = component_results[1:]
                    idx = 0
                    for rx in component_results:
                        op = operators[idx]
                        if op == "<&&>":
                            component_ok = component_ok and rx
                        elif op == "<||>":
                            component_ok = component_ok or rx

                        idx += 1

                expression_results.append(component_ok)

            if len(expression_results) == 1:
                condition_ok = expression_results[0]
            else:
                condition_ok = expression_results[0]
                component_results = expression_results[1:]
                for rx in expression_results:
                    condition_ok = condition_ok and rx

            if condition_ok:
                request.trace.append(
                    f"success condition: {cit.id}, kvs id: {cit.kvs_id_ok}")

                request.ok = True

                if cit.kvs_id_ok != 0:
                    rs = RunRuleResult(rule, None, [])
                    rs.kv = self._repo.kvs.read(cit.kvs_id_ok)
                    rs.kvitems = self._repo.kvitem.read_by_parent_id(
                        cit.kvs_id_ok)
                    request.rule_results.append(rs)
                break

        if not condition_ok:
            request.trace.append("failed")

            if rule.kvs_id_nok != 0:
                rs = RunRuleResult(rule, None, [])
                rs.kv = self._repo.kvs.read(rule.kvs_id_nok)
                rs.kvitems = self._repo.kvitem.read_by_parent_id(
                    rule.kvs_id_nok)
                request.rule_results.append(rs)

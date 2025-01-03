""" _module_ """
from typing import List
from domain.entities import Parameter, Case, Condition, KVItem
from .parameter import ParameterModel
from .case import CaseModel
from .condition import ConditionModel
from .kv_item import KVItemModel


class RuleModel:
    """ Rule Model """

    def __init__(
            self, tenantid, _id, name, rule_type, strategy, version, is_active, parameters: List[Parameter], cases: List[Case], conditions: List[Condition], kv_items: List[KVItem]):
        self.tenant_id = tenantid
        self.id = _id
        self.name = name
        self.rule_type = rule_type
        self.strategy = strategy
        self.version = version
        self.is_active = is_active

        self.cases = []
        self.conditions = []
        self.kvitems = []
        self.parameters = []

        if isinstance(parameters, list):
            for p in parameters:
                one_param = ParameterModel(
                    p.key, p.rule_id, p.usefor, p.typeof)
                self.parameters.append(one_param.__dict__)

        if isinstance(cases, list):
            for c in cases:
                one_case = CaseModel(
                    c.id, c.rule_id, c.position, c.condition_group_id, c.kvs_id, c.is_active)
                self.cases.append(one_case.__dict__)

        if isinstance(conditions, list):
            for c in conditions:
                one_cond = ConditionModel(
                    c.variable, c.condition_group_id, c.operator, c.value, c.is_case_sensitive, c.typeof, c.is_active)
                self.conditions.append(one_cond.__dict__)

        if isinstance(kv_items, list):
            for e in kv_items:
                one_item = KVItemModel(
                    e.key, e.kv_id, e.value, e.calculation, e.typeof, c.is_active)
                self.kvitems.append(one_item.__dict__)


class KVItemModel:
    """ KV Item Model """

    def __init__(self, key, kv_id, value, calculation, typeof, is_active):
        self.key = key
        self.kv_id = kv_id
        self.value = value
        self.calculation = calculation
        self.typeof = typeof
        self.is_active = is_active


class ConditionModel:
    """ Condition  Model """

    def __init__(self, variable, condition_group_id, operator, value, is_case_sensitive, typeof, is_active):
        self.variable = variable
        self.condition_group_id = condition_group_id
        self.operator = operator
        self.value = value
        self.is_case_sensitive = is_case_sensitive
        self.typeof = typeof
        self.is_active = is_active


class CaseModel:
    """ Case Model """

    def __init__(self, _id, rule_id, position, condition_group_id, kvs_id, is_active):
        self.id = _id
        self.rule_id = rule_id
        self.position = position
        self.condition_group_id = condition_group_id
        self.kvs_id = kvs_id
        self.is_active = is_active


class ParameterModel:
    """ Parameter Model """

    def __init__(self, key: str, rule_id: str, usefor: str, typeof: str):
        self.key = key
        self.rule_id = rule_id
        self.usefor = usefor
        self.typeof = typeof

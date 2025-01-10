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
            self,
            tenantid,
            _id,
            name,
            rule_type,
            strategy,
            version,
            is_active,
            parameters: List[Parameter],
            cases: List[Case],
            conditions: List[Condition],
            kv_items: List[KVItem]
    ):
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
                    c.variable, c.condition_group_id, c.operator, c.value, c.typeof, c.is_active)
                self.conditions.append(one_cond.__dict__)

        if isinstance(kv_items, list):
            for e in kv_items:
                one_item = KVItemModel(
                    e.key, e.kv_id, e.value, e.calculation, e.typeof, c.is_active)
                self.kvitems.append(one_item.__dict__)

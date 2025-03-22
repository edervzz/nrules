
export * from "./TenantDto"
export * from "./CreateRuleDto"
export * from "./RuleDto"
export * from "./ErrorDto"
export * from "./ParameterDto"
export * from "./NewCaseDto"
export * from "./UpdCaseDto"
export * from "./CaseDto"
export * from "./TagDto"
export * from "./NewParameterDto"
export * from "./NewParametersDto"
export * from "./UpdConditionDto"
export * from "./UpdKVItemDto"

export type NewRuleCondition = {
    id:string;
    variable: string;
    type: string;
};

export type NewRuleOutput = {
    id:string;
    variable: string;
    type: string;
};

export type NewRuleTag = {
    id:string;
    key:string;
    value: string;
};






export * from "./TenantDto"
export * from "./CreateRuleDto"
export * from "./RuleDto"
export * from "./ErrorDto"
export * from "./ParameterDto"
export * from "./CaseDto"
export * from "./TagDto"

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





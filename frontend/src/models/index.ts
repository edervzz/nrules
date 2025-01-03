
export * from "./TenantDto"
export * from "./CreateRuleDto"
export * from "./ErrorDto"
export * from "./ParameterDto"
export * from "./Case"

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





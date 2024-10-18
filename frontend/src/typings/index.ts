export * from "./RuleDto"
export * from "./TenantDto"
export * from "./CreateRuleDto"

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


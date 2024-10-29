
export * from "./TenantDto"
export * from "./CreateRuleDto"
export * from "./ErrorDto"
export * from "./ParameterDto"
export * from "./PaginationDto"

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




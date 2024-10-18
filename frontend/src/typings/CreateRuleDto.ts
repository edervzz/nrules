export type CreateRuleDto = {
    name: string,
    strategy: string,
    rule_type: string,
    parameters?: ParametersDto[]
}


export type ParametersDto = {
    key: string,
    typeof: string,
    usefor: string
}

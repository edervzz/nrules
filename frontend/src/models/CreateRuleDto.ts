import { ParametersDto } from "./ParameterDto"

export type CreateRuleDto = {
    name: string,
    strategy: string,
    rule_type: string,
    parameters?: ParametersDto[]
}

export type ReadRuleDto = {
    id: string,
    name: string,
    strategy: string,
    rule_type: string,
    default_kvs?: number,
    version: number,
    parameters?: ParametersDto[]
}

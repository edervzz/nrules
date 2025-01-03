import { ParametersDto } from "./ParameterDto"
import { TagDto } from "./TagDto"

export type CreateRuleDto = {
    name: string,
    strategy: string,
    rule_type: string,
    parameters?: ParametersDto[],
    tags?: TagDto[]
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

import { ParametersDto } from "./ParameterDto"
import { CaseDto } from "./CaseDto"
import { ConditionDto } from "./ConditionDto"
import { KVItemDto } from "./KVItemDto"


export type RuleDto = {
    id: string,
    name: string,
    rule_type: string,
    strategy: string,
    version: number,
    is_active: boolean,

    cases?: CaseDto[],
    
    conditions?: ConditionDto[]
    
    kvitems?: KVItemDto[],
    
    parameters?: ParametersDto[]
}


import { ParametersDto } from "./CreateRuleDto"

export type CreateRuleDto = {
    name: string
    rule_type: string
    strategy: string
    parameters: ParametersDto[]
}

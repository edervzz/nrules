export type Case = {
    expressions: ExpressionDto[]
    outputs: OutputDto[]
}

export type ExpressionDto = {
    variable: string,
    operator: string,
    value: string
}

export type OutputDto = {
    key: string,
    value: string
}



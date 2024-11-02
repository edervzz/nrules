export enum Operator {
    EQ = 1,
    NE,
    GT,
    LT,
    GE,
    LE,
    IN,
    NI,
    BT,
    NB,
    ANY,
}

export enum OperatorDto {
    EQ = "=",
    NE = "<>",
    GT = ">",
    LT = "<",
    GE = ">=",
    LE = "<=>",
    IN = "IN",
    NI = "NI",
    BT = "BT",
    NB = "NB",
    ANY = "ANY",
}

export enum ConditionType {
    STR = "String",
    NUM = "Numeric",
    BOOL = "Boolean",
    DATE = "Date",
    TIME = "Time",
    DTIME = "Datetime",
}

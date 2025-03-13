export const INPUT = "INPUT";
export const OUTPUT = "OUTPUT";

export const STRING = "STRING";
export const NUMERIC = "NUMERIC";
export const DATE = "DATE";
export const JSON = "JSON";
export const FN = "FN";

export const EQ = "EQ";
export const NE = "NE";
export const GT = "GT";
export const GE = "GE";
export const LT = "LT";
export const LE = "LE";
export const IN = "IN";
export const NI = "NI";
export const BT = "BT";
export const NB = "NB";
export const ANY = "ANY";
export const ELSE = "ELSE";

export const EQ_SYM = "=";
export const NE_SYM = "!=";
export const GT_SYM = ">";
export const LT_SYM = "<";
export const GE_SYM = ">=";
export const LE_SYM = "<=";
export const IN_SYM = "[..]";
export const NI_SYM = "] [";
export const BT_SYM = "<->";
export const NB_SYM = "> <";
export const ANY_SYM = "*";
export const ELSE_SYM = "ELSE";

export function typeofparam(t: string) {
    switch (t) {
        case STRING:
            return <i className="bi bi-alphabet-uppercase"></i>;
        case NUMERIC:
            return <i className="bi bi-123"></i>;
        case DATE:
            return <i className="bi bi-calendar-day"></i>;
        case JSON:
            return <i className="bi bi-filetype-json"></i>;
    }
}

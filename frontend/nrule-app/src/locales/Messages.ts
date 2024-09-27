import i18next from "./i18n";

i18next.changeLanguage("es");

export default class Messages{
    static SELECT_OPERATOR = i18next.t("common:select_operator");

    static EQUAL = i18next.t("common:equal");
    static NOT_EQUAL = i18next.t("common:not_equal");
    static LESS_EQUAL = i18next.t("common:less_equal");
    static GREATER_EQUAL = i18next.t("common:greater_equal");
    static LESS_THAN = i18next.t("common:less_than");
    static GREATER_THAN = i18next.t("common:greater_than");
    static IN = i18next.t("common:in_");
    static NOT_IN = i18next.t("common:not_in");
    static BETWEEN = i18next.t("common:between");
    static NOT_BETWEEN = i18next.t("common:not_between");
    static ANY = i18next.t("common:any");
    static EQUAL_DESC = i18next.t("common:equal_desc");
    static NOT_EQUAL_DESC = i18next.t("common:not_equal_desc");
    static LESS_THAN_DESC = i18next.t("common:less_than_desc");
    static GREATER_THAN_DESC = i18next.t("common:greater_than_desc");
    static LESS_EQUAL_DESC = i18next.t("common:less_equal_desc");
    static GREATER_EQUAL_DESC = i18next.t("common:greater_equal_desc");
    static IN_DESC = i18next.t("common:in_desc");
    static NOT_IN_DESC = i18next.t("common:not_in_desc");
    static BETWEEN_DESC = i18next.t("common:between_desc");
    static NOT_BETWEEN_DESC = i18next.t("common:not_between_desc");
    static ANY_DESC = i18next.t("common:any_desc");

    static EQ = "="
    static NE = "<>"
    static GT = ">"
    static LT = "<"
    static GE = ">="
    static LE = "<="
    static I = "In"
    static E = "Ex"
    static BT = "[ . ]"
    static NB = "] ["
    static ANYVAL = "*"
}

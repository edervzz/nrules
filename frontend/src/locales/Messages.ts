import i18next from "./i18n";

export default class Messages{

    static CREA_RULE_001 = i18next.t("common:crea_rule_001");

    static NAME = i18next.t("common:name");
    static TYPE = i18next.t("common:type");

    static START_NEW_RULE = i18next.t("common:start_new_rule");
    static INPUT_PARAMS = i18next.t("common:input_params");
    static OUTPUT_PARAMS = i18next.t("common:output_params");
    static SEND_CREA_RULE = i18next.t("common:send_crea_rule");

    static BUTTON_OUTPUT = i18next.t("common:button_output");
    static BUTTON_CONDITION = i18next.t("common:button_condition");
    static BUTTON_ADD = i18next.t("common:button_add");
    static BUTTON_CONTINUE = i18next.t("common:button_continue");
    static BUTTON_NEXT = i18next.t("common:button_next");
    static BUTTON_BACK = i18next.t("common:button_back");
    static BUTTON_CANCEL = i18next.t("common:button_cancel");
    static BUTTON_CLOSE = i18next.t("common:button_close");
    
    
    static SETTINGS = i18next.t("common:settings");
    static SIGN_OUT = i18next.t("common:sign_out");
    static NEW_RULE = i18next.t("common:new_rule");
    static NEW_RULE_PARAMS = i18next.t("common:new_rule_params");
    static RULENAME = i18next.t("common:rulename");
    static RULETYPE = i18next.t("common:ruletype");
    static RULETYPE_SELECT = i18next.t("common:ruletype_select");
    static TABLE = i18next.t("common:table");
    static TREE = i18next.t("common:tree");
    static FLOW = i18next.t("common:flow");
    static TABLES = i18next.t("common:tables");
    static TREES = i18next.t("common:trees");
    static FLOWS = i18next.t("common:flows");
    static MANAGEMENT = i18next.t("common:management");
    static TRANSPORTS = i18next.t("common:transports");
    static TENANTS = i18next.t("common:tenants");
    static USERS = i18next.t("common:users");
    static SELECT_OPERATOR = i18next.t("common:select_operator");

    // operators descriptions
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

    // operators
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

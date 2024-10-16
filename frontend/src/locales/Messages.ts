import i18n from "../locales/i18n";

export default class Messages{

    static get CREA_RULE_001():string { return i18n.t("common:crea_rule_001"); }

    static get NAME():string { return i18n.t("common:name"); }
    static get TYPE():string { return i18n.t("common:type"); }

    static get START_NEW_RULE():string { return i18n.t("common:start_new_rule"); }
    static get INPUT_PARAMS():string { return i18n.t("common:input_params"); }
    static get OUTPUT_PARAMS():string { return i18n.t("common:output_params"); }
    static get SEND_CREA_RULE():string { return i18n.t("common:send_crea_rule"); }

    static get BUTTON_OUTPUT():string { return i18n.t("common:button_output"); }
    static get BUTTON_CONDITION():string { return i18n.t("common:button_condition"); }
    static get BUTTON_ADD():string { return i18n.t("common:button_add"); }
    static get BUTTON_CONTINUE():string { return i18n.t("common:button_continue"); }
    static get BUTTON_NEXT():string { return i18n.t("common:button_next"); }
    static get BUTTON_BACK():string { return i18n.t("common:button_back"); }
    static get BUTTON_CANCEL():string { return i18n.t("common:button_cancel"); }
    static get BUTTON_CLOSE():string { return i18n.t("common:button_close"); }
    
    static get CONNECTING():string { return i18n.t("common:connecting"); }
    static get SOME_WRONG():string { return i18n.t("common:some_wrong"); }
    static get ERROR_USR_PWD():string { return i18n.t("common:error_user_pwd"); }

    static get TENANTID():string { return i18n.t("common:tenant_id"); }
    static get USERNAME():string { return i18n.t("common:username"); }
    static get PASSWORD():string { return i18n.t("common:password"); }
    static get LOGIN():string { return i18n.t("common:login"); }

    static get NRULE_INFO():string { return i18n.t("common:nrule_info"); }
    static get NRULE_HELP():string { return i18n.t("common:nrule_help"); }
    static get NRULE_SPECS():string { return i18n.t("common:nrule_specs"); }
    static get NRULE_CAPABILITIES():string { return i18n.t("common:nrule_capabilities"); }
    static get NRULE_TO_START():string { return i18n.t("common:nrule_to_start"); } 
    
    static get SETTINGS():string { return i18n.t("common:settings"); }
    static get SIGN_OUT():string { return i18n.t("common:sign_out"); }
    static get NEW_RULE():string { return i18n.t("common:new_rule"); }
    static get NEW_RULE_PARAMS():string { return i18n.t("common:new_rule_params"); }
    static get RULENAME():string { return i18n.t("common:rulename"); }
    static get RULESTRATEGY():string { return i18n.t("common:rulestrategy"); }
    static get RULESTRATEGY_SELECT():string { return i18n.t("common:rulestrategy_select"); }
    static get RULESTRATEGY_EARLY():string { return i18n.t("common:rulestrategy_early"); }
    static get RULESTRATEGY_BASE():string { return i18n.t("common:rulestrategy_base"); }
    static get RULESTRATEGY_ALL():string { return i18n.t("common:rulestrategy_all"); }
    static get RULETYPE():string { return i18n.t("common:ruletype"); }
    static get RULETYPE_SELECT():string { return i18n.t("common:ruletype_select"); }
    static get TABLE():string { return i18n.t("common:table"); }
    static get TREE():string { return i18n.t("common:tree"); }
    static get FLOW():string { return i18n.t("common:flow"); }
    static get RULES():string { return i18n.t("common:rules"); }
    static get TABLES():string { return i18n.t("common:tables"); }
    static get TREES():string { return i18n.t("common:trees"); }
    static get FLOWS():string { return i18n.t("common:flows"); }
    static get RUNNER():string { return i18n.t("common:runner"); }
    static get MANAGEMENT():string { return i18n.t("common:management"); }
    static get TRANSPORTS():string { return i18n.t("common:transports"); }
    static get TENANTS():string { return i18n.t("common:tenants"); }
    static get USERS():string { return i18n.t("common:users"); }
    static get SELECT_OPERATOR():string { return i18n.t("common:select_operator"); }

    // operators descriptions
    static get EQUAL():string { return i18n.t("common:equal"); }
    static get NOT_EQUAL():string { return i18n.t("common:not_equal"); }
    static get LESS_EQUAL():string { return i18n.t("common:less_equal"); }
    static get GREATER_EQUAL():string { return i18n.t("common:greater_equal"); }
    static get LESS_THAN():string { return i18n.t("common:less_than"); }
    static get GREATER_THAN():string { return i18n.t("common:greater_than"); }
    static get IN():string { return i18n.t("common:in_"); }
    static get NOT_IN():string { return i18n.t("common:not_in"); }
    static get BETWEEN():string { return i18n.t("common:between"); }
    static get NOT_BETWEEN():string { return i18n.t("common:not_between"); }
    static get ANY():string { return i18n.t("common:any"); }
    static get EQUAL_DESC():string { return i18n.t("common:equal_desc"); }
    static get NOT_EQUAL_DESC():string { return i18n.t("common:not_equal_desc"); }
    static get LESS_THAN_DESC():string { return i18n.t("common:less_than_desc"); }
    static get GREATER_THAN_DESC():string { return i18n.t("common:greater_than_desc"); }
    static get LESS_EQUAL_DESC():string { return i18n.t("common:less_equal_desc"); }
    static get GREATER_EQUAL_DESC():string { return i18n.t("common:greater_equal_desc"); }
    static get IN_DESC():string { return i18n.t("common:in_desc"); }
    static get NOT_IN_DESC():string { return i18n.t("common:not_in_desc"); }
    static get BETWEEN_DESC():string { return i18n.t("common:between_desc"); }
    static get NOT_BETWEEN_DESC():string { return i18n.t("common:not_between_desc"); }
    static get ANY_DESC():string { return i18n.t("common:any_desc"); }

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

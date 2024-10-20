import i18n from "../locales/i18n";

export default class Messages{

    static get CREA_RULE_001():string { return i18n.t("common:crea_rule_001"); }

    static get OUTNAME_DEFAULT():string { return i18n.t("common:outname_default"); }
    static get CONDNAME():string { return i18n.t("common:cond_name"); }
    static get OUTNAME():string { return i18n.t("common:out_name"); }
    static get NAME():string { return i18n.t("common:name"); }
    static get TYPE():string { return i18n.t("common:type"); }

    static get BUTTON_OUTPUT_DEFAULT():string { return i18n.t("common:button_output_default"); }
    static get BUTTON_OUTPUT():string { return i18n.t("common:button_output"); }
    static get BUTTON_CONDITION():string { return i18n.t("common:button_condition"); }
    static get BUTTON_ADD():string { return i18n.t("common:button_add"); }
    static get BUTTON_CONTINUE():string { return i18n.t("common:button_continue"); }
    static get BUTTON_NEXT():string { return i18n.t("common:button_next"); }
    static get BUTTON_BACK():string { return i18n.t("common:button_back"); }
    static get BUTTON_CANCEL():string { return i18n.t("common:button_cancel"); }
    static get BUTTON_CLOSE():string { return i18n.t("common:button_close"); }
    
    static get NEWRULE_CREA_RULE():string { return i18n.t("common:newrule_create_rule"); }
    static get NEWRULE_RULENAME():string { return i18n.t("common:newrule_rulename"); }
    static get NEWRULE_RULESTRATEGY():string { return i18n.t("common:newrule_rulestrategy"); }
    static get NEWRULE_RULESTRATEGY_SELECT():string { return i18n.t("common:newrule_rulestrategy_select"); }
    static get NEWRULE_RULESTRATEGY_EARLY():string { return i18n.t("common:newrule_rulestrategy_early"); }
    static get NEWRULE_RULESTRATEGY_BASE():string { return i18n.t("common:newrule_rulestrategy_base"); }
    static get NEWRULE_RULESTRATEGY_ALL():string { return i18n.t("common:newrule_rulestrategy_all"); }
    static get NEWRULE_RULETYPE():string { return i18n.t("common:newrule_ruletype"); }
    static get NEWRULE_RULETYPE_SELECT():string { return i18n.t("common:newrule_ruletype_select"); }
    
    static get MENUBAR_NEW_RULE():string { return i18n.t("common:menubar_new_rule"); }
    static get MENUBAR_MATRIXES():string { return i18n.t("common:menubar_matrixes"); }
    static get MENUBAR_RUNNER():string { return i18n.t("common:menubar_runner"); }
    static get MENUBAR_MANAGEMENT():string { return i18n.t("common:menubar_management"); }
    static get MENUBAR_TRANSPORTS():string { return i18n.t("common:menubar_transports"); }
    static get MENUBAR_TENANTS():string { return i18n.t("common:menubar_tenants"); }
    static get MENUBAR_SIGN_OUT():string { return i18n.t("common:menubar_sign_out"); }
    static get MENUBAR_LOGING_OUT():string { return i18n.t("common:menubar_loging_out"); }

    static get MESSAGE_SOME_WRONG():string { return i18n.t("common:message_some_wrong"); }
    static get MESSAGE_CONNECTING():string { return i18n.t("common:message_connecting"); }
    static get MESSAGE_LOADING():string { return i18n.t("common:message_loading"); }
    static get MESSAGE_ERROR_USR_PWD():string { return i18n.t("common:message_error_user_pwd"); }
    
    static get LOGIN_TENANTID():string { return i18n.t("common:login_tenant_id"); }
    static get LOGIN_USERNAME():string { return i18n.t("common:login_username"); }
    static get LOGIN_PASSWORD():string { return i18n.t("common:login_password"); }
    static get LOGIN_LOGIN():string { return i18n.t("common:login_login"); }

    static get NRULE_INFO():string { return i18n.t("common:nrule_info"); }
    static get NRULE_HELP():string { return i18n.t("common:nrule_help"); }
    static get NRULE_SPECS():string { return i18n.t("common:nrule_specs"); }
    static get NRULE_CAPABILITIES():string { return i18n.t("common:nrule_capabilities"); }
    static get NRULE_TO_START():string { return i18n.t("common:nrule_to_start"); }     
    
    static get COMMON_MATRIX():string { return i18n.t("common:common_matrix"); }
    static get COMMON_SELECT_OPERATOR():string { return i18n.t("common:common_select_operator"); }

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

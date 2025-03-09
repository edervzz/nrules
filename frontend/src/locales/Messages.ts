import i18n from "../locales/i18n";

export default class Messages{

    static get CREA_RULE_001():string { return i18n.t("common:crea_rule_001"); }

    static get OUTNAME_DEFAULT():string { return i18n.t("common:outname_default"); }
    static get EXPRESSIONS():string { return i18n.t("common:expressions"); }
    static get EXPRESSION():string { return i18n.t("common:expression"); }
    static get EXPRESSIONNAME():string { return i18n.t("common:expression_name"); }
    static get ADDEXPRESSION():string { return i18n.t("common:add_expression"); }
    static get CASES():string { return i18n.t("common:cases"); }
    static get CONDITIONS():string { return i18n.t("common:conditions"); }
    static get CONDITION():string { return i18n.t("common:condition"); }
    static get CONDITIONNAME():string { return i18n.t("common:condition_name"); }
    static get ADDCONDITION():string { return i18n.t("common:add_condition"); }
    static get OUTPUTS():string { return i18n.t("common:outputs"); }
    static get OUTPUT():string { return i18n.t("common:output"); }
    static get OUTPUTNAME():string { return i18n.t("common:output_name"); }
    static get ROW():string { return i18n.t("common:row"); }
    static get ARCHIVE():string { return i18n.t("common:archive"); }
    static get ADDOUTPUT():string { return i18n.t("common:add_output"); }
    static get NAME():string { return i18n.t("common:name"); }
    static get TYPE():string { return i18n.t("common:type"); }
    static get TAGS():string { return i18n.t("common:tags"); }
    static get KEY():string { return i18n.t("common:key"); }
    static get VALUE():string { return i18n.t("common:value"); }
    static get BYDFAULT():string { return i18n.t("common:bydefault"); }

    static get BUTTON_OUTPUT_DEFAULT():string { return i18n.t("common:button_output_default"); }
    static get BUTTON_OUTPUT():string { return i18n.t("common:button_output"); }
    static get BUTTON_CONDITION():string { return i18n.t("common:button_condition"); }
    static get BUTTON_ADD():string { return i18n.t("common:button_add"); }
    static get BUTTON_CONTINUE():string { return i18n.t("common:button_continue"); }
    static get BUTTON_NEXT():string { return i18n.t("common:button_next"); }
    static get BUTTON_BACK():string { return i18n.t("common:button_back"); }
    static get BUTTON_CANCEL():string { return i18n.t("common:button_cancel"); }
    static get BUTTON_CLOSE():string { return i18n.t("common:button_close"); }
    static get BUTTON_FIRST():string { return i18n.t("common:button_first"); }
    static get BUTTON_LAST():string { return i18n.t("common:button_last"); }
    
    static get NEWRULE_CREA_RULE():string { return i18n.t("common:newrule_create_rule"); }
    static get NEWRULE_RULENAME():string { return i18n.t("common:newrule_rulename"); }
    static get NEWRULE_RULESTRATEGY():string { return i18n.t("common:newrule_rulestrategy"); }
    static get NEWRULE_RULESTRATEGY_SELECT():string { return i18n.t("common:newrule_rulestrategy_select"); }
    static get NEWRULE_RULESTRATEGY_EARLY():string { return i18n.t("common:newrule_rulestrategy_early"); }
    static get NEWRULE_RULESTRATEGY_BASE():string { return i18n.t("common:newrule_rulestrategy_base"); }
    static get NEWRULE_RULESTRATEGY_ALL():string { return i18n.t("common:newrule_rulestrategy_all"); }
    static get NEWRULE_RULETYPE():string { return i18n.t("common:newrule_ruletype"); }
    static get NEWRULE_RULETYPE_SELECT():string { return i18n.t("common:newrule_ruletype_select"); }
    static get NEWRULE_STATUS():string { return i18n.t("common:newrule_status"); }
    static get NEWRULE_INFO_01():string { return i18n.t("common:newrule_info_01"); }
    static get NEWRULE_INFO_02():string { return i18n.t("common:newrule_info_02"); }
    
    static get MENUBAR_NEW_RULE():string { return i18n.t("common:menubar_new_rule"); }
    static get MENUBAR_RULES():string { return i18n.t("common:menubar_rules"); }
    static get MENUBAR_MATRIXES():string { return i18n.t("common:menubar_matrixes"); }
    static get MENUBAR_RUNNER():string { return i18n.t("common:menubar_runner"); }
    static get MENUBAR_MANAGEMENT():string { return i18n.t("common:menubar_management"); }
    static get MENUBAR_GO():string { return i18n.t("common:menubar_go"); }
    static get MENUBAR_TRANSPORTS():string { return i18n.t("common:menubar_transports"); }
    static get MENUBAR_TENANTS():string { return i18n.t("common:menubar_tenants"); }
    static get MENUBAR_SIGN_OUT():string { return i18n.t("common:menubar_sign_out"); }
    static get MENUBAR_LOGING_OUT():string { return i18n.t("common:menubar_loging_out"); }

    static get MATRIX_INFO():string { return i18n.t("common:matrix_info"); }

    static get MESSAGE_SOME_WRONG():string { return i18n.t("common:message_some_wrong"); }
    static get MESSAGE_CONNECTING():string { return i18n.t("common:message_connecting"); }
    static get MESSAGE_LOADING():string { return i18n.t("common:message_loading"); }
    static get MESSAGE_ERROR_USR_PWD():string { return i18n.t("common:message_error_user_pwd"); }
    
    static get LOGIN_TENANTID():string { return i18n.t("common:login_tenant_id"); }
    static get LOGIN_USERNAME():string { return i18n.t("common:login_username"); }
    static get LOGIN_PASSWORD():string { return i18n.t("common:login_password"); }
    static get LOGIN_LOGIN():string { return i18n.t("common:login_login"); }    
    static get TOOLBAR_SEARCH(): string {return i18n.t("common:toolbar_search")}

    static get NRULE():string { return i18n.t("common:nrule"); }
    static get NRULE_INFO():string { return i18n.t("common:nrule_info"); }
    static get NRULE_HELP():string { return i18n.t("common:nrule_help"); }
    static get NRULE_SPECS():string { return i18n.t("common:nrule_specs"); }
    static get NRULE_CAPABILITIES():string { return i18n.t("common:nrule_capabilities"); }
    static get NRULE_TO_START():string { return i18n.t("common:nrule_to_start"); }     
    
    static get COMMON_TABLE():string { return i18n.t("common:common_matrix"); }
    static get COMMON_TREE():string { return i18n.t("common:common_tree"); }
    static get COMMON_SELECT_OPERATOR():string { return i18n.t("common:common_select_operator"); }
    static get COMMON_SENDING():string { return i18n.t("common:common_sending"); }
    static get COMMON_OF():string { return i18n.t("common:common_of"); }

    static get EDITOR():string { return i18n.t("common:editor"); }
    static get DISPLAY():string { return i18n.t("common:display"); }
    static get UPDATE():string { return i18n.t("common:update"); }
    static get FINISH():string { return i18n.t("common:finish"); }
    static get ACTIONS():string { return i18n.t("common:actions"); }
    static get TABLES():string { return i18n.t("common:tables"); }
    static get TREES():string { return i18n.t("common:trees"); }
    static get ARCHIVED():string { return i18n.t("common:archived"); }



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

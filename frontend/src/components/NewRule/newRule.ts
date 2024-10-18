import Joi from "joi";
import Messages from "../../locales/Messages";

export function ruleTypeText(rulename: string, ruletype: number) {
    switch (ruletype) {
        case 1:
            return Messages.MATRIX + ": " + rulename;
        case 2:
            return Messages.TREE + ": " + rulename;
    }
    return rulename;
}

export function validateHeader(rulename: string ){
    const schema = Joi.object({
        runame: Joi.string()
            .alphanum()
            .min(5)
            .max(50)
            .required()
            .error((_)=>new Error(Messages.CREA_RULE_001)),
    });

    const result = schema.validate({runame: rulename})
    return result.error?.message
}

export function titleNewRule(step:number){
    switch (step) {
        case 1:
            return Messages.START_NEW_RULE;
        case 2:
            return Messages.INPUT_PARAMS;
        case 3:
            return Messages.OUTPUT_PARAMS;
        default:
            return Messages.SEND_CREA_RULE;
    }
}

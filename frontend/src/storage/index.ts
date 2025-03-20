import { RuleAdapter } from "./RuleAdapter";
import { CaseAdapter } from "./CaseAdapter"
import { ParameterAdapter } from "./ParameterAdapter"
import { ConditionAdapter } from "./ConditionAdapter"

export default class Storage{
    public static Rule: RuleAdapter = new RuleAdapter;
    public static Case: CaseAdapter = new CaseAdapter;
    public static Parameter: ParameterAdapter = new ParameterAdapter;
    public static Condition: ConditionAdapter = new ConditionAdapter;
}

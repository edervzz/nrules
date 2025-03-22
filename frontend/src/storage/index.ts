import { RuleAdapter } from "./RuleAdapter";
import { CaseAdapter } from "./CaseAdapter"
import { ParameterAdapter } from "./ParameterAdapter"
import { ConditionAdapter } from "./ConditionAdapter"
import { KVItemAdapter } from "./KVItemAdapter"

export default class Storage{
    public static Rule: RuleAdapter = new RuleAdapter;
    public static Case: CaseAdapter = new CaseAdapter;
    public static Parameter: ParameterAdapter = new ParameterAdapter;
    public static Condition: ConditionAdapter = new ConditionAdapter;
    public static KVItem: KVItemAdapter = new KVItemAdapter;
}

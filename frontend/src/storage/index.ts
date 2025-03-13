import { RuleAdapter } from "./RuleAdapter";
import { CaseAdapter } from "./CaseAdapter"
import { ParameterAdapter } from "./ParameterAdapter"

export default class Storage{
    public static Rule: RuleAdapter = new RuleAdapter;
    public static Case: CaseAdapter = new CaseAdapter;
    public static Parameter: ParameterAdapter = new ParameterAdapter;
}

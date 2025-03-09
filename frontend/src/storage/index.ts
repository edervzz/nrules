import { RuleAdapter } from "./RuleAdapter";
import { CaseAdapter } from "./CaseAdapter"

export default class Storage{
    public static Rule: RuleAdapter = new RuleAdapter;
    public static Case: CaseAdapter = new CaseAdapter;
}

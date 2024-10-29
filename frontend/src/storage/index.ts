
import EnvarsSession, { EnvarsLocal } from "../envars";
import { RuleAdapter } from "./RuleAdapter";

export default class Storage{
    static Rule: RuleAdapter = new RuleAdapter;

    static Session: EnvarsSession = new EnvarsSession;

    static Local : EnvarsLocal = new EnvarsLocal;
}

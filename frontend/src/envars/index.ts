import { CreateRuleDto, TenantDto } from "../models";

export default class EnvarsSession{
    // session storage
    clear(){
        sessionStorage.clear();
    }

    get tenant(){
        const t =  sessionStorage.getItem("tenant") || "";
        if (t === ""){
            return {
                id: 0,
                username: "",
                tenantName: "",
                tokenDev: "",
                tokenTest: "",
                tokenProd: "",
            }
        }
        return JSON.parse(t) as TenantDto;
    }

    set tenant(value:TenantDto){
        sessionStorage.setItem("tenant",JSON.stringify(value));
    }

    set ruleInProgress(value:CreateRuleDto){
        sessionStorage.setItem("ruleInProgress",JSON.stringify(value));
    }

    get ruleInProgress(){
        const r = sessionStorage.getItem("ruleInProgress") || "";
        if (r === ""){
            return {
                name:"",rule_type:"",strategy:"",parameters: [],
            }
        }
        return JSON.parse(r) as CreateRuleDto
    }

}

export class EnvarsLocal{
    get language(){
        return localStorage.getItem("langu") || "es";
    }

    set language(value:string){
        localStorage.setItem("langu",value);
    }
}

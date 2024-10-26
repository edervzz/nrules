import { CreateRuleDto, TenantDto } from "../typings";

export default class Vars{
    // session storage
    public static clear(){
        sessionStorage.clear();
    }

    public static get tenant(){
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

    public static set tenant(value:TenantDto){
        sessionStorage.setItem("tenant",JSON.stringify(value));
    }

    public static set ruleInProgress(value:CreateRuleDto){
        sessionStorage.setItem("ruleInProgress",JSON.stringify(value));
    }

    public static get ruleInProgress(){
        const r = sessionStorage.getItem("ruleInProgress") || "";
        if (r === ""){
            return {
                id: "",name:"",rule_type:"",strategy:"",tenant_id:0, parameters: [],
            }
        }
        return JSON.parse(r) as CreateRuleDto
    }

    // local storage
    public static get language(){
        return localStorage.getItem("langu") || "es";
    }

    public static set language(value:string){
        localStorage.setItem("langu",value);
    }

    
}

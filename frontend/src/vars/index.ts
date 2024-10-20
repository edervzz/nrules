export default class Vars{
    public static get tenant(){
        return sessionStorage.getItem("tenant") || "";
    }

    public static set tenant(value:string){
        sessionStorage.setItem("tenant",value);
    }

    public static get language(){
        return localStorage.getItem("langu") || "es";
    }

    public static set language(value:string){
        localStorage.setItem("langu",value);
    }

    public static clear(){
        sessionStorage.clear();
    }
}

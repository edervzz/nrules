export default class Session{
    public static get tenant(){
        return sessionStorage.getItem("tenant") || "";
    }

    public static set tenant(value:string){
        sessionStorage.setItem("tenant",value);
    }

    public static clear(){
        sessionStorage.clear();
    }
}

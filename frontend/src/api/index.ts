import axios, { AxiosError } from "axios";
import { ResultAPI } from "../typings";
import Vars from "../vars";

const host = import.meta.env.VITE_API_URL_HOST + "/nr/api/" + import.meta.env.VITE_API_VER;

export const CREA_RULE = (tid: string) => `${host}/t/${tid}/rules`
export const READ_RULES_PAGE = (tid: string, no:string, size:string, search:string) => {
    let word = ""
    if (search!=="") word = `&word=${search}`
    return `${host}/t/${tid}/rules?pageNo=${no}&pageSize=${size}${word}`
}

export async function CallGet<T>(url: string): Promise<ResultAPI<T>>{
    try {
        const res = await axios.get<T>(url, {
            headers: {
                "Accept-Language": Vars.language,
            },
        });
        
        const nextPage = res.headers!["next-page"] || 0;
        const prevPage = res.headers!["previous-page"] || 0;
        const totalPages = res.headers!["total-pages"] || 0;
        const totalCount = res.headers!["total-count"] || 0;
    
        return {
            data: res.data,
            nextPage: nextPage,
            prevPage: prevPage,
            totalPages: totalPages,
            totalCount:totalCount,
            ok: true,
            errorMessage: ""
        } as ResultAPI<T>;
    } catch (error) {
        const err = error as AxiosError;
        return {
            data: undefined,
            ok: false,
            errorMessage: err.message
        } as ResultAPI<T>;
    }
}

export async function CallPost<T>(url: string, data: any): Promise<ResultAPI<T>>{
    try {
        const res = await axios.post<T>(url, data, {
            headers: {
                "Accept-Language": Vars.language,
            },
        });
        const item = res.headers!["item"] || "";
        return {
            data: res.data,
            item: item,
            ok: true,
            errorMessage: ""
        } as ResultAPI<T>;
    } catch (error) {
        const err = error as AxiosError;
        return {
            data: undefined,
            ok: false,
            errorMessage: err.message
        } as ResultAPI<T>;
    }

}

import axios, { AxiosError } from "axios";
import Env from "../env";
import { ErrorDto } from "../models";

const basepath = import.meta.env.VITE_API_URL_HOST + "/nr/api/" + import.meta.env.VITE_API_VER + "/t/" + Env.tenant.id.toString(); 

export async function _CallPost(url: string, data: any): Promise<ResultPost>{
    try {
        const res = await axios.post(basepath + url, data, {
            headers: {
                "Accept-Language": Env.language,
            },
        });
        
        return {
            item: res.headers["item"] || "",
            ok: true,
            errorMessage: ""
        } as ResultPost;
    } catch (error) {
        const err = error as AxiosError;
        return {
            ok: false,
            errorMessage: err.message,
            errorList:  err.response?.data as ErrorDto[]
        } as ResultPost
    }

}

export async function _CallGet<T>(url: string): Promise<ResultGetPage<T>>{
    try {        
        const res = await axios.get<T>(basepath + url, {
            headers: {
                "Accept-Language": Env.language,
            },
        });
        return {
            ok: true,
            nextPage: res.headers["next-page"] || 0,
            prevPage : res.headers["previous-page"] || 0,
            totalPages : res.headers["total-pages"] || 0,
            totalCount : res.headers["total-count"] || 0, 
            data: res.data,
        } as ResultGetPage<T>;
    } catch (error) {
        const err = error as AxiosError;
        return {
            data: undefined,
            ok: false,
            status: err.status,
            errorMessage: err.message,
            errorList:  err.response?.data as ErrorDto[]
        } as ResultGetPage<T>;
    }
}

export type ResultPost= {
    item?: string,
    ok: boolean,
    errorMessage?: string,
    errorList?: ErrorDto[]
}

export type ResultGetPage<T> = {
    ok: boolean,
    status: number,
    data?: T,
    nextPage: number,
    prevPage: number,
    totalPages: number,
    totalCount: number,
    errorMessage?: string,
    errorList?: ErrorDto[]
}

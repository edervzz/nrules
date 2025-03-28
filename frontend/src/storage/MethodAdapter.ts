import axios, { AxiosError } from "axios";
import { ErrorListDto } from "../models";
import EnvarsSession, { EnvarsLocal } from "../envars";

const basepath = import.meta.env.VITE_API_URL_HOST + "/nr/api/" + import.meta.env.VITE_API_VER + "/t/" + EnvarsSession.tenant.id.toString(); 

export async function _CallPost<T>(url: string, data?: T): Promise<ResultPost>{
    try {
        
        const res = await axios.post(basepath + url, data, {
            headers: {
                "Accept-Language": EnvarsLocal.language,
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
            errorList:  err.response?.data as ErrorListDto
        } as ResultPost
    }

}

export async function _CallPut<T>(url: string, data: T): Promise<ResultPost>{
    try {
        const res = await axios.put(basepath + url, data, {
            headers: {
                "Accept-Language": EnvarsLocal.language,
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
            errorList:  err.response?.data as ErrorListDto
        } as ResultPost
    }

}

export async function _CallGet<T>(url: string): Promise<ResultGetPage<T>>{
    try {        
        const res = await axios.get<T>(basepath + url, {
            headers: {
                "Accept-Language": EnvarsLocal.language,
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
            errorList:  err.response?.data as ErrorListDto
        } as ResultGetPage<T>;
    }
}

export type ResultPost= {
    item?: string,
    ok: boolean,
    errorMessage?: string,
    errorList?: ErrorListDto
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
    errorList?: ErrorListDto
}

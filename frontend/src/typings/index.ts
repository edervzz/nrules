import { AxiosResponseHeaders, RawAxiosResponseHeaders } from "axios";

export * from "./RuleDto"
export * from "./TenantDto"
export * from "./CreateRuleDto"
export * from "./ErrorDto"

export type NewRuleCondition = {
    id:string;
    variable: string;
    type: string;
};


export type NewRuleOutput = {
    id:string;
    variable: string;
    type: string;
};

export type Pagination = {
    currentPageNo: number,
    nextPageNo: number,
    prevPageNo: number,
    pageSize: number,
    totalPages: number,
    totalCount: number,
}

export type ResultAPI<T> = {
    data?: T,
    nextPage: number,
    prevPage: number,
    totalPages: number,
    totalCount: number,
    item: string,
    ok: boolean,
    errorMessage: string
}

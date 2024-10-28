import { ReadRuleDto } from "../models";
import { _CallGet, _CallPost, ResultGetPage, ResultPost } from "./MethodAdapter";

export async function PostRule(data: any): Promise<ResultPost>{
    const url = `/rules`;
    
    const result = await _CallPost(url,data);
    return result;
}

export async function GetRulesPaged(pageno:number = 1, pagesize:number = 10, search:string = ""): Promise<ResultGetPage<ReadRuleDto[]>>{
    const url = `/rules?pageNo=${pageno}&pageSize=${pagesize}${search==="" ? "" : `&word=${search}`}`
    
    const result = await _CallGet<ReadRuleDto[]>(url);
    return result;
}

export async function GetRule(ruleid: string): Promise<ResultGetPage<ReadRuleDto>>{
    const url = `/rules/${ruleid}`
    
    const result = await _CallGet<ReadRuleDto>(url);
    return result;
}

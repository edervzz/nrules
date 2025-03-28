import { CreateRuleDto, RuleDto } from "../models";
import { _CallGet, _CallPost, ResultGetPage, ResultPost } from "./MethodAdapter";

export class RuleAdapter{
    async PostRule(data: CreateRuleDto): Promise<ResultPost>{
        const url = `/rules`;
        
        const result = await _CallPost(url,data);
        return result;
    }

    async GetRulesPaged(pageno:number = 1, pagesize:number = 10, search:string = ""): Promise<ResultGetPage<RuleDto[]>>{
        const url = `/rules?pageNo=${pageno}&pageSize=${pagesize}${search==="" ? "" : `&word=${search}`}`
        
        const result = await _CallGet<RuleDto[]>(url);
        return result;
    }

    async GetRule(ruleid: string): Promise<ResultGetPage<RuleDto>>{
        const url = `/rules/${ruleid}`
        
        const result = await _CallGet<RuleDto>(url);
        return result;
    }

    async PostCheckRule(ruleid: string): Promise<ResultPost>{
        const url = `/rules/${ruleid}/check`;
        
        const result = await _CallPost(url);
        return result;
    }
}

import { UpdItemsCaseDto, NewCaseDto } from "../models";
import { _CallPost, _CallGet, _CallPut, ResultPost } from "./MethodAdapter";

export class CaseAdapter{
    async PutCase(ruleid: string, data: UpdItemsCaseDto): Promise<ResultPost>{
        const url = `/rules/${ruleid}/cases`;
        
        const result = await _CallPut(url,data);
        return result;
    }

    async PostCase(ruleid: string, data: NewCaseDto): Promise<ResultPost>{
        const url = `/rules/${ruleid}/cases`;
        
        const result = await _CallPost(url,data);
        return result;
    }

}

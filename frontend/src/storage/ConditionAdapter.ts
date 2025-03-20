import { UpdItemsConditionDto } from "../models";
import { _CallPost, _CallGet, _CallPut, ResultPost } from "./MethodAdapter";

export class ConditionAdapter{
    async PutCondition(ruleid: string, caseid: string, data: UpdItemsConditionDto): Promise<ResultPost>{
        const url = `/rules/${ruleid}/cases/${caseid}/conditions`;
        
        const result = await _CallPut(url,data);
        return result;
    }

}

import { NewParametersDto } from "../models";
import { _CallPost, _CallGet, _CallPut, ResultPost } from "./MethodAdapter";

export class ParameterAdapter{
    
    async PostCase(ruleid: string, data: NewParametersDto): Promise<ResultPost>{
        const url = `/rules/${ruleid}/parameters`;
        
        const result = await _CallPost(url,data);
        return result;
    }

}

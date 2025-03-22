import { UpdItemsKVItemDto } from "../models";
import { _CallPost, _CallGet, _CallPut, ResultPost } from "./MethodAdapter";

export class KVItemAdapter{
    async PutKVItems(ruleid: string, caseid: string, data: UpdItemsKVItemDto): Promise<ResultPost>{
        const url = `/rules/${ruleid}/cases/${caseid}/kv-items`;
        
        const result = await _CallPut(url,data);
        return result;
    }

}

import { v4 as uuidv4 } from "uuid";
import { NewRuleCondition, NewRuleOutput } from "../../models";
import { ConditionType } from "../../enums";

export const HandleAddCondition = (
    conditions: NewRuleCondition[], 
    setConditions: React.Dispatch<React.SetStateAction<NewRuleCondition[]>>
) => {
    const condition: NewRuleCondition = {
        id: uuidv4(),
        variable: "",
        type: ConditionType.STR,
    };
    const newConditions = [...conditions, { ...condition }];
    setConditions(newConditions);
};

export const handleChangeCondition = (
    conditions: NewRuleCondition[], 
    setConditions: React.Dispatch<React.SetStateAction<NewRuleCondition[]>>, 
    id: string, 
    value: string
) => {
    setConditions(
        conditions.map((x) => (x.id === id ? { ...x, variable: value } : x))
    );
};

export const handleChangeConditionType = (
    conditions: NewRuleCondition[], 
    setConditions: React.Dispatch<React.SetStateAction<NewRuleCondition[]>>,
    id: string, 
    value: string
) => {
    setConditions(
        conditions.map((x) => (x.id === id ? { ...x, type: value } : x))
    );
};

export const handleDelCondition = (
    conditions: NewRuleCondition[], 
    setConditions: React.Dispatch<React.SetStateAction<NewRuleCondition[]>>,
    id: string
) => {
    setConditions(conditions.filter((x) => x.id !== id));
};

export const handleAddOutput = (
    outputs: NewRuleOutput[], 
    setOutputs: React.Dispatch<React.SetStateAction<NewRuleOutput[]>>
) => {
    const output: NewRuleOutput = {
        id: uuidv4(),
        variable: "",
        type: ConditionType.STR,
    };
    setOutputs([...outputs, { ...output }]);
};

export const handleChangeOutput = (
    outputs: NewRuleOutput[], 
    setOutputs: React.Dispatch<React.SetStateAction<NewRuleOutput[]>>,
    id: string, 
    value: string
) => {
    setOutputs(
        outputs.map((x) => (x.id === id ? { ...x, variable: value } : x))
    );
};

export const handleChangeOutputType = (
    outputs: NewRuleOutput[], 
    setOutputs: React.Dispatch<React.SetStateAction<NewRuleOutput[]>>,
    id: string, 
    value: string
) => {
    setOutputs(
        outputs.map((x) => (x.id === id ? { ...x, type: value } : x))
    );
};

export const handleDelOutput = (outputs: NewRuleOutput[], 
    setOutputs: React.Dispatch<React.SetStateAction<NewRuleOutput[]>>, 
    id: string
) => {
    setOutputs(outputs.filter((x) => x.id !== id));
};

export const handleClose = (setShowSending: React.Dispatch<React.SetStateAction<boolean>>) => {
    setShowSending(false);
};



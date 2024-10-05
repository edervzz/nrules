import { NewRuleCondition } from "../../../typings";
import Step01 from "./Step01";
import Step02 from "./Step02";

type Props = {
    currentStep: Number;
    rulename: string;
    ruletype: number;
    handleRulenameChange: (v: string) => void;
    handleRuleTypeChange: (v: number) => void;
    isError: boolean;
    conditions: NewRuleCondition[];
    onDelete: (id: number) => void;
    onChangeVariable: (id: number, value: string) => void;
    onChangeType: (id: number, value: string) => void;
    onAdd: () => void;
};

export default function Steps({
    currentStep,
    rulename,
    ruletype,
    handleRulenameChange,
    handleRuleTypeChange,
    isError,
    conditions,
    onDelete,
    onChangeVariable,
    onChangeType,
    onAdd,
}: Props) {
    switch (currentStep) {
        case 1:
            return (
                <Step01
                    rulename={rulename}
                    ruletype={ruletype}
                    onRuleNameChange={handleRulenameChange}
                    onRuleTypeChange={handleRuleTypeChange}
                    isError={isError}
                />
            );
        case 2:
            return (
                <Step02
                    conditions={conditions}
                    onDelete={onDelete}
                    onChangeVariable={onChangeVariable}
                    onChangeType={onChangeType}
                    onAdd={onAdd}
                />
            );
    }
    return <></>;
}

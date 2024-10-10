import { NewRuleCondition, NewRuleOutput } from "../../../typings";
import Step01 from "./Step01";
import Step02 from "./Step02";
import Step03 from "./Step03";
import Step04 from "./Step04";

type Props = {
    currentStep: Number;
    rulename: string;
    ruletype: number;
    rulestrategy: number;
    handleRulenameChange: (v: string) => void;
    handleRuleTypeChange: (v: number) => void;
    handleRuleStrategyChange: (v: number) => void;
    isError: boolean;
    conditions: NewRuleCondition[];
    onAddCondition: () => void;
    onChangeCondition: (id: number, value: string) => void;
    onChangeConditionType: (id: number, value: string) => void;
    onDeleteCondition: (id: number) => void;
    outputs: NewRuleOutput[];
    onAddOutput: () => void;
    onChangeOutput: (id: number, value: string) => void;
    onChangeOutputType: (id: number, value: string) => void;
    onDeleteOutput: (id: number) => void;
};

export default function Steps({
    currentStep,
    rulename,
    ruletype,
    rulestrategy,
    handleRulenameChange,
    handleRuleTypeChange,
    handleRuleStrategyChange,
    isError,
    conditions,
    onAddCondition,
    onChangeCondition,
    onChangeConditionType,
    onDeleteCondition,
    outputs,
    onAddOutput,
    onChangeOutput,
    onChangeOutputType,
    onDeleteOutput,
}: Props) {
    switch (currentStep) {
        case 1:
            return (
                <Step01
                    rulename={rulename}
                    ruletype={ruletype}
                    rulestrategy={rulestrategy}
                    onRuleNameChange={handleRulenameChange}
                    onRuleTypeChange={handleRuleTypeChange}
                    onRuleStrategyChange={handleRuleStrategyChange}
                    isError={isError}
                />
            );
        case 2:
            return (
                <Step02
                    conditions={conditions}
                    onAddCondition={onAddCondition}
                    onChangeCondition={onChangeCondition}
                    onChangeConditionType={onChangeConditionType}
                    onDeleteCondition={onDeleteCondition}
                />
            );
        case 3:
            return (
                <Step03
                    outputs={outputs}
                    onAddOutput={onAddOutput}
                    onChangeOutput={onChangeOutput}
                    onChangeOutputType={onChangeOutputType}
                    onDeleteOutput={onDeleteOutput}
                />
            );
        case 4:
            return (
                <Step04
                    rulename={rulename}
                    ruletype={ruletype}
                    conditions={conditions}
                    outputs={outputs}
                />
            );
    }
    return <></>;
}

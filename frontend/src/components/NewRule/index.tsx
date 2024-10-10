import { Button, Modal } from "react-bootstrap";
import ProgressBar from "react-bootstrap/ProgressBar";
import Messages from "../../locales/Messages";
import { useState } from "react";
import { titleNewRule, validateHeader } from "./newRule";
import Steps from "./Steps";
import { NewRuleCondition, NewRuleOutput } from "../../typings";
import { ConditionType } from "../../enums";

type Props = {
    onHide: () => void;
};

const totalSteps = 4;

function NewRule({ onHide }: Props) {
    // 1. states
    const [currentStep, setCurrentStep] = useState(1);

    const [disableNextButton, setDisableNextButton] = useState(true);

    const [isError, setIsError] = useState(false);

    const [headerRule, setHeaderRule] = useState({
        rulename: "",
        ruletype: 0,
        rulestrategy: 0,
    });
    const [conditionsRule, setConditionsRule] = useState<NewRuleCondition[]>([
        { id: 1, variable: "", type: ConditionType.STR },
    ]);

    const [outputsRule, setOutputRule] = useState<NewRuleOutput[]>([
        { id: 1, variable: "", type: ConditionType.STR },
    ]);

    // 2. event handlers
    const handleNext = () => {
        const errorMessage = validateHeader(headerRule.rulename);

        if (errorMessage == undefined && headerRule.ruletype != 0) {
            currentStep + 1 <= totalSteps && setCurrentStep(currentStep + 1);
            setIsError(false);
        } else {
            if (headerRule.rulename.length >= 5) {
                setIsError(false);
            } else {
                setIsError(true);
            }
        }
    };

    const handleBack = () =>
        currentStep - 1 <= 0 ? onHide() : setCurrentStep(currentStep - 1);

    // 2.1. Header
    const handleRulenameChange = (v: string) => {
        setHeaderRule({ ...headerRule, rulename: v });
        setDisableNextButton(
            headerRule.rulestrategy == 0 ||
                headerRule.ruletype == 0 ||
                headerRule.rulename.length <= 5
        );
    };

    const handleRuleTypeChange = (v: number) => {
        setHeaderRule({ ...headerRule, ruletype: v });
        setDisableNextButton(
            headerRule.rulestrategy != 0 &&
                headerRule.ruletype != 0 &&
                headerRule.rulename.length >= 5
        );
    };

    const handleRuleStrategyChange = (v: number) => {
        setHeaderRule({ ...headerRule, rulestrategy: v });
        setDisableNextButton(
            headerRule.rulestrategy != 0 &&
                headerRule.ruletype != 0 &&
                headerRule.rulename.length >= 5
        );
    };

    // 2.3. Conditions
    const handleAddCondition = () => {
        const condition: NewRuleCondition = {
            id: conditionsRule.length + 1,
            variable: "",
            type: ConditionType.STR,
        };
        const newasdf = [...conditionsRule, { ...condition }];

        setConditionsRule(newasdf);
    };

    const handleChangeCondition = (id: number, value: string) => {
        setConditionsRule(
            conditionsRule.map((x) =>
                x.id === id ? { ...x, variable: value } : x
            )
        );
    };
    const handleChangeConditionType = (id: number, value: string) => {
        setConditionsRule(
            conditionsRule.map((x) => (x.id === id ? { ...x, type: value } : x))
        );
    };

    const handleDeleteCondition = (id: number) => {
        setConditionsRule(conditionsRule.filter((x) => x.id !== id));
    };

    // 2.4. Outputs
    const handleAddOutput = () => {
        const output: NewRuleOutput = {
            id: outputsRule.length + 1,
            variable: "",
            type: ConditionType.STR,
        };
        setOutputRule([...outputsRule, { ...output }]);
    };

    const handleChangeOutput = (id: number, value: string) => {
        setOutputRule(
            outputsRule.map((x) =>
                x.id === id ? { ...x, variable: value } : x
            )
        );
    };
    const handleChangeOutputType = (id: number, value: string) => {
        setOutputRule(
            outputsRule.map((x) => (x.id === id ? { ...x, type: value } : x))
        );
    };

    const handleDeleteOuput = (id: number) => {
        setOutputRule(outputsRule.filter((x) => x.id !== id));
    };

    // 3. jsx
    return (
        <Modal
            size="lg"
            show={true}
            onHide={onHide}
            backdrop="static"
            keyboard={currentStep !== totalSteps}
        >
            <Modal.Header closeButton>
                <Modal.Title>{titleNewRule(currentStep)}</Modal.Title>
            </Modal.Header>

            <Modal.Body>
                <ProgressBar now={(currentStep / totalSteps) * 100} />
                <Steps
                    currentStep={currentStep}
                    rulename={headerRule.rulename}
                    ruletype={headerRule.ruletype}
                    rulestrategy={headerRule.rulestrategy}
                    handleRulenameChange={handleRulenameChange}
                    handleRuleTypeChange={handleRuleTypeChange}
                    handleRuleStrategyChange={handleRuleStrategyChange}
                    isError={isError}
                    conditions={conditionsRule}
                    onAddCondition={handleAddCondition}
                    onChangeCondition={handleChangeCondition}
                    onChangeConditionType={handleChangeConditionType}
                    onDeleteCondition={handleDeleteCondition}
                    outputs={outputsRule}
                    onAddOutput={handleAddOutput}
                    onChangeOutput={handleChangeOutput}
                    onChangeOutputType={handleChangeOutputType}
                    onDeleteOutput={handleDeleteOuput}
                />
            </Modal.Body>

            <Modal.Footer>
                <Button
                    onClick={handleBack}
                    variant="secondary"
                    hidden={currentStep == totalSteps}
                >
                    {Messages.BUTTON_BACK}
                </Button>
                <Button
                    onClick={handleNext}
                    variant="primary"
                    disabled={disableNextButton}
                    hidden={currentStep == totalSteps}
                >
                    {Messages.BUTTON_NEXT}
                </Button>
            </Modal.Footer>
        </Modal>
    );
}

export default NewRule;

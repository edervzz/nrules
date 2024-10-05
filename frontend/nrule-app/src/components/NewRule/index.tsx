import { Button, Modal } from "react-bootstrap";
import Messages from "../../locales/Messages";
import { useState } from "react";
import { ruleTypeText, validateHeader } from "./newRule";
import Steps from "./Steps";
import { NewRuleCondition } from "../../typings";
import { ConditionType } from "../../enums/operator";

type Props = {
    onHide: () => void;
};

function NewRule({ onHide }: Props) {
    // 1. define states
    const [headerRule, setHeaderRule] = useState({
        rulename: "",
        ruletype: 0,
    });
    const [conditionsRule, setConditionsRule] = useState<NewRuleCondition[]>([
        { id: 1, variable: "", type: ConditionType.STR },
    ]);

    const [currentStep, setCurrentStep] = useState(1);

    const [isError, setIsError] = useState(false);

    const [disableNextButton, setDisableNextButton] = useState(true);

    // 2. define event handlers
    const handleRulenameChange = (v: string) => {
        setHeaderRule({ ...headerRule, rulename: v });
        setDisableNextButton(
            headerRule.ruletype == 0 || headerRule.rulename.length < 5
        );
    };

    const handleRuleTypeChange = (v: number) => {
        setHeaderRule({ ...headerRule, ruletype: v });
        setDisableNextButton(
            headerRule.ruletype != 0 && headerRule.rulename.length >= 5
        );
    };

    const handleChangeVariable = (id: number, value: string) => {
        setConditionsRule(
            conditionsRule.map((x) =>
                x.id === id ? { ...x, variable: value } : x
            )
        );
    };

    const handleChangeType = (id: number, value: string) => {
        setConditionsRule(
            conditionsRule.map((x) => (x.id === id ? { ...x, type: value } : x))
        );
    };

    const handleAdd = () => {
        const condition: NewRuleCondition = {
            id: conditionsRule.length + 1,
            variable: "",
            type: ConditionType.STR,
        };
        const newasdf = [...conditionsRule, { ...condition }];
        console.log(newasdf);

        setConditionsRule(newasdf);
    };

    const handleDelete = (id: number) => {
        setConditionsRule(conditionsRule.filter((x) => x.id !== id));
    };

    const handleNext = () => {
        const errorMessage = validateHeader(headerRule.rulename);

        if (errorMessage == undefined && headerRule.ruletype != 0) {
            currentStep + 1 <= 2 && setCurrentStep(currentStep + 1);
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

    // 3. jsx element
    return (
        <Modal
            size="lg"
            show={true}
            onHide={onHide}
            backdrop="static"
            keyboard={true}
        >
            <Modal.Header closeButton>
                <Modal.Title>
                    {currentStep == 1
                        ? Messages.NEW_RULE
                        : ruleTypeText(
                              headerRule.rulename,
                              headerRule.ruletype
                          )}
                </Modal.Title>
            </Modal.Header>

            <Modal.Body>
                <Steps
                    currentStep={currentStep}
                    rulename={headerRule.rulename}
                    ruletype={headerRule.ruletype}
                    handleRulenameChange={handleRulenameChange}
                    handleRuleTypeChange={handleRuleTypeChange}
                    isError={isError}
                    conditions={conditionsRule}
                    onDelete={handleDelete}
                    onChangeVariable={handleChangeVariable}
                    onChangeType={handleChangeType}
                    onAdd={handleAdd}
                />
            </Modal.Body>

            <Modal.Footer>
                <Button variant="secondary" onClick={handleBack}>
                    {Messages.BUTTON_BACK}
                </Button>
                <Button
                    disabled={disableNextButton}
                    variant="primary"
                    onClick={handleNext}
                >
                    {Messages.BUTTON_NEXT}
                </Button>
            </Modal.Footer>
        </Modal>
    );
}

export default NewRule;

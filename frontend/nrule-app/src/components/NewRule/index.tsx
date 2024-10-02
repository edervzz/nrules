import { Button, Modal } from "react-bootstrap";
import Messages from "../../locales/Messages";
import { useState } from "react";
import Steps from "./Steps";

type Props = {
    onHide: () => void;
};

function NewRule({ onHide }: Props) {
    const [step, setStep] = useState(1);

    const handleNext = () => step + 1 <= 2 && setStep(step + 1);

    const handleBack = () => (step - 1 <= 0 ? onHide() : setStep(step - 1));

    return (
        <Modal show={true} onHide={onHide}>
            <Modal.Header closeButton>
                <Modal.Title>
                    {step == 1 ? Messages.NEW_RULE : Messages.NEW_RULE_PARAMS}
                </Modal.Title>
            </Modal.Header>

            <Modal.Body>
                <Steps step={step} />
            </Modal.Body>

            <Modal.Footer>
                <Button variant="secondary" onClick={handleBack}>
                    {Messages.BUTTON_BACK}
                </Button>
                <Button variant="primary" onClick={handleNext}>
                    {Messages.BUTTON_NEXT}
                </Button>
            </Modal.Footer>
        </Modal>
    );
}

export default NewRule;

import { Button, Form, InputGroup, Modal } from "react-bootstrap";
import Messages from "../../locales/Messages";
import { useRef } from "react";
import { ConditionType } from "../../enums";

type Props = {
    title: string;
    onClose: () => void;
    onAddParameter: (
        name: string | undefined,
        type: string | undefined
    ) => void;
};

const AddParameter = ({ title, onAddParameter, onClose }: Props) => {
    const refParamName = useRef<HTMLInputElement>(null);
    const refParamType = useRef<HTMLSelectElement>(null);
    return (
        <Modal show>
            <Modal.Header closeButton onHide={onClose}>
                <Modal.Title>{title}</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <InputGroup className="mb-3">
                    <Form.Control
                        ref={refParamName}
                        aria-label="First name"
                        placeholder={Messages.NAME}
                    />
                </InputGroup>
                <Form.Select
                    title={Messages.TYPE}
                    ref={refParamType}
                    aria-label="Default select example"
                >
                    <option>{ConditionType.STR}</option>
                    <option>{ConditionType.NUM}</option>
                    <option>{ConditionType.BOOL}</option>
                    <option>{ConditionType.DATE}</option>
                </Form.Select>
            </Modal.Body>
            <Modal.Footer>
                <Button
                    variant="primary"
                    onClick={() => {
                        onAddParameter(
                            refParamName.current?.value,
                            refParamType.current?.value
                        );
                    }}
                >
                    <i className="bi bi-check-lg"></i>
                </Button>
            </Modal.Footer>
        </Modal>
    );
};

export default AddParameter;

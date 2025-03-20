import { Button, Col, Container, Form, Modal, Row } from "react-bootstrap";
import Messages from "../../locales/Messages";
import { DATE, NUMERIC, STRING } from "../../tools";
import { useRef } from "react";

interface Props {
    onSubmit?: (name: string, type: string) => void;
    onCancel?: () => void;
}

const ConditionForm = ({ onSubmit: onOk, onCancel: onNotOk }: Props) => {
    const nameRef = useRef<HTMLInputElement>(null);
    const typeRef = useRef<HTMLSelectElement>(null);

    return (
        <Modal size="sm" show backdrop="static" keyboard={false}>
            <Form
                onSubmit={(e) => {
                    e.preventDefault();
                    onOk?.(
                        nameRef.current?.value || "",
                        typeRef.current?.value || ""
                    );
                }}
            >
                <Modal.Header>
                    <Modal.Title>{Messages.ADDCONDITION}</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Container className="d-flex justify-content-center">
                        <Form.Group className="mb-3">
                            <Form.Label>{Messages.CONDITIONNAME}</Form.Label>
                            <Form.Control
                                aria-label="Default select example"
                                ref={nameRef}
                            ></Form.Control>
                            <br></br>
                            <Form.Label>{Messages.DATATYPE}</Form.Label>
                            <Form.Select
                                aria-label="Default select example"
                                ref={typeRef}
                            >
                                <option value={STRING}>{STRING}</option>
                                <option value={NUMERIC}>{NUMERIC}</option>
                                <option value={DATE}>{DATE}</option>
                            </Form.Select>
                        </Form.Group>
                    </Container>
                </Modal.Body>
                <Modal.Footer>
                    <Row>
                        <Col className="text-end">
                            <Button
                                variant="secondary"
                                className="me-2"
                                onClick={() => onNotOk?.()}
                            >
                                {Messages.BUTTON_CANCEL}
                            </Button>
                            <Button variant="primary" type="submit">
                                {Messages.BUTTON_NEXT}
                            </Button>
                        </Col>
                    </Row>
                </Modal.Footer>
            </Form>
        </Modal>
    );
};

export default ConditionForm;

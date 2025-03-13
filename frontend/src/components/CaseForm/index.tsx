import { Button, Col, Container, Form, Modal, Row } from "react-bootstrap";
import Messages from "../../locales/Messages";
import { useState } from "react";

type Props = {
    totalCases: number;
    onSubmit: (pos: number) => void;
    onCancel: () => void;
};

function CaseForm({ totalCases, onSubmit, onCancel }: Props) {
    const [casePos, setCasePos] = useState(totalCases.toString());

    return (
        <Modal show size="sm" backdrop="static" keyboard={false}>
            <Modal.Header>
                <Modal.Title>{Messages.NEWCASE}</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Container className="d-flex justify-content-center">
                    <Form.Group
                        className="mb-3"
                        controlId="exampleForm.ControlInput1"
                    >
                        <Form.Label>
                            {Messages.NEWCASEPOS +
                                " " +
                                Messages.NEWCASEBETWEEN +
                                "[1 - " +
                                totalCases +
                                "]"}
                        </Form.Label>
                        <Form.Control
                            value={casePos}
                            onChange={(e) => {
                                setCasePos(e.currentTarget.value);
                            }}
                            placeholder={
                                Messages.NEWCASEBETWEEN + "1 - " + totalCases
                            }
                        ></Form.Control>
                    </Form.Group>
                </Container>
            </Modal.Body>
            <Modal.Footer>
                <Row>
                    <Col className="text-end">
                        <Button
                            variant="secondary"
                            className="me-2"
                            onClick={(_) => onCancel()}
                        >
                            {Messages.BUTTON_CANCEL}
                        </Button>
                        <Button
                            variant="primary"
                            onClick={(_) => onSubmit(parseInt(casePos))}
                        >
                            {Messages.BUTTON_NEXT}
                        </Button>
                    </Col>
                </Row>
            </Modal.Footer>
        </Modal>
    );
}

export default CaseForm;

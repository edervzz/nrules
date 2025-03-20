import { Button, Col, Container, Modal, Row } from "react-bootstrap";
import Messages from "../../locales/Messages";
import styles from "./Operator.module.css";
import { EQ, NE, LT, LE, GT, GE, IN, EX, BT, NB, ANY } from "../../tools";

type Props = {
    onCancel?: () => void;
    onSelectOperator?: (op: string) => void;
};

function Operator({ onCancel, onSelectOperator }: Props) {
    return (
        <div style={{ fontFamily: "monospace" }}>
            <Modal show size="lg" backdrop="static" keyboard={false}>
                <Modal.Header>{Messages.COMMON_SELECT_OPERATOR}</Modal.Header>
                <Modal.Body>
                    <Container>
                        <Row>
                            <Col xs="1">
                                <Button
                                    onClick={(_) => onSelectOperator?.(EQ)}
                                    variant="outline-primary"
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    {EQ}
                                </Button>
                            </Col>
                            <Col>{Messages.EQUAL_DESC}</Col>
                            <Col xs="1">
                                <Button
                                    onClick={(_) => onSelectOperator?.(IN)}
                                    variant="outline-primary"
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    {IN}
                                </Button>
                            </Col>
                            <Col>{Messages.IN_DESC}</Col>
                        </Row>
                        <Row className="mt-3">
                            <Col xs="1">
                                <Button
                                    onClick={(_) => onSelectOperator?.(NE)}
                                    variant="outline-primary"
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    {NE}
                                </Button>
                            </Col>
                            <Col>{Messages.NOT_EQUAL_DESC}</Col>
                            <Col xs="1">
                                <Button
                                    onClick={(_) => onSelectOperator?.(EX)}
                                    variant="outline-primary"
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    {EX}
                                </Button>
                            </Col>
                            <Col>{Messages.NOT_IN_DESC}</Col>
                        </Row>
                        <Row className="mt-3">
                            <Col xs="1">
                                <Button
                                    onClick={(_) => onSelectOperator?.(GT)}
                                    variant="outline-primary"
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    {GT}
                                </Button>
                            </Col>
                            <Col>{Messages.GREATER_THAN_DESC}</Col>
                            <Col xs="1">
                                <Button
                                    onClick={(_) => onSelectOperator?.(BT)}
                                    variant="outline-primary"
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    {BT}
                                </Button>
                            </Col>
                            <Col>{Messages.BETWEEN_DESC}</Col>
                        </Row>
                        <Row className="mt-3">
                            <Col xs="1">
                                <Button
                                    onClick={(_) => onSelectOperator?.(LT)}
                                    variant="outline-primary"
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    {LT}
                                </Button>
                            </Col>
                            <Col>{Messages.LESS_THAN_DESC}</Col>
                            <Col xs="1">
                                <Button
                                    onClick={(_) => onSelectOperator?.(NB)}
                                    variant="outline-primary"
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    {NB}
                                </Button>
                            </Col>
                            <Col>{Messages.NOT_BETWEEN_DESC}</Col>
                        </Row>
                        <Row className="mt-3">
                            <Col xs="1">
                                <Button
                                    onClick={(_) => onSelectOperator?.(GE)}
                                    variant="outline-primary"
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    {GE}
                                </Button>
                            </Col>
                            <Col>{Messages.GREATER_EQUAL_DESC}</Col>
                            <Col xs="1">
                                <Button
                                    onClick={(_) => onSelectOperator?.(ANY)}
                                    variant="outline-primary"
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    {ANY}
                                </Button>
                            </Col>
                            <Col>{Messages.ANY_DESC}</Col>
                        </Row>
                        <Row className="mt-3">
                            <Col xs="1">
                                <Button
                                    onClick={(_) => onSelectOperator?.(LE)}
                                    variant="outline-primary"
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    {LE}
                                </Button>
                            </Col>
                            <Col>{Messages.LESS_EQUAL_DESC}</Col>
                            <Col></Col>
                            <Col></Col>
                        </Row>
                    </Container>
                </Modal.Body>
                <Modal.Footer>
                    <Row>
                        <Col className="text-end">
                            <Button
                                variant="secondary"
                                className="me-2"
                                onClick={(_) => {
                                    onCancel?.();
                                }}
                            >
                                {Messages.BUTTON_CANCEL}
                            </Button>
                        </Col>
                    </Row>
                </Modal.Footer>
            </Modal>
        </div>
    );
}

export default Operator;

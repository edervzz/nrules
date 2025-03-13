import {
    Button,
    Col,
    Container,
    Form,
    Modal,
    Row,
    Table,
} from "react-bootstrap";
import Messages from "../../locales/Messages";
import { useState } from "react";
import styles from "./Operator.module.css";

type Props = {};

function Operator({}: Props) {
    return (
        <div style={{ fontFamily: "monospace" }}>
            <Modal show size="lg" backdrop="static" keyboard={false}>
                <Modal.Header>{Messages.COMMON_SELECT_OPERATOR}</Modal.Header>
                <Modal.Body>
                    <Container>
                        <Row>
                            <Col xs="1">
                                <Button
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    EQ
                                </Button>
                            </Col>
                            <Col>{Messages.EQUAL_DESC}</Col>
                            <Col xs="1">
                                <Button
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    IN
                                </Button>
                            </Col>
                            <Col>{Messages.IN_DESC}</Col>
                        </Row>
                        <Row className="mt-3">
                            <Col xs="1">
                                <Button
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    NE
                                </Button>
                            </Col>
                            <Col>{Messages.NOT_EQUAL_DESC}</Col>
                            <Col xs="1">
                                <Button
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    NI
                                </Button>
                            </Col>
                            <Col>{Messages.NOT_IN_DESC}</Col>
                        </Row>
                        <Row className="mt-3">
                            <Col xs="1">
                                <Button
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    GT
                                </Button>
                            </Col>
                            <Col>{Messages.GREATER_THAN_DESC}</Col>
                            <Col xs="1">
                                <Button
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    BT
                                </Button>
                            </Col>
                            <Col>{Messages.BETWEEN_DESC}</Col>
                        </Row>
                        <Row className="mt-3">
                            <Col xs="1">
                                <Button
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    LT
                                </Button>
                            </Col>
                            <Col>{Messages.LESS_THAN_DESC}</Col>
                            <Col xs="1">
                                <Button
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    NB
                                </Button>
                            </Col>
                            <Col>{Messages.NOT_BETWEEN_DESC}</Col>
                        </Row>
                        <Row className="mt-3">
                            <Col xs="1">
                                <Button
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    GE
                                </Button>
                            </Col>
                            <Col>{Messages.GREATER_EQUAL_DESC}</Col>
                            <Col xs="1">
                                <Button
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    ANY
                                </Button>
                            </Col>
                            <Col>{Messages.ANY_DESC}</Col>
                        </Row>
                        <Row className="mt-3">
                            <Col xs="1">
                                <Button
                                    className={`${styles.myButton}`}
                                    size="sm"
                                >
                                    LE
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
                            <Button variant="secondary" className="me-2">
                                {Messages.BUTTON_CANCEL}
                            </Button>
                            <Button variant="primary">
                                {Messages.BUTTON_NEXT}
                            </Button>
                        </Col>
                    </Row>
                </Modal.Footer>
            </Modal>
        </div>
    );
}

export default Operator;

import {
    Button,
    Col,
    Container,
    Form,
    Modal,
    OverlayTrigger,
    Row,
    Tooltip,
} from "react-bootstrap";
import { Operator } from "../../enums";
import { useState } from "react";
import BasicOperatorSelector from "../BasicOperatorSelector";
import Messages from "../../locales/Messages";

interface Props {
    operator: Operator;
    betweenText: string;
    onOperationConditionSelected: (op: Operator) => void;
}

const Conditionsss = ({ operator, onOperationConditionSelected }: Props) => {
    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
    const handleOperatorSelected = (op: Operator) => {
        onOperationConditionSelected(op);
        handleClose();
    };

    const [operatorSymbol, operatorText] = getOperatorSymbol(operator);
    const renderTooltip = <Tooltip id="tooltip">{operatorText}</Tooltip>;
    return (
        <Container fluid>
            <Row xs="auto">
                <Col
                    xs={1}
                    style={{
                        backgroundColor: "gray",
                        paddingTop: 5,
                    }}
                >
                    <OverlayTrigger
                        placement="bottom"
                        delay={{ show: 250, hide: 400 }}
                        overlay={renderTooltip}
                    >
                        <Button
                            size="sm"
                            onClick={handleShow}
                            variant="success"
                        >
                            {operatorSymbol}
                        </Button>
                    </OverlayTrigger>
                </Col>
                <Col style={{ backgroundColor: "blue", padding: "2" }}>
                    <Form.Control
                        type="text"
                        placeholder="Value"
                        disabled={operator === Operator.ANY ? true : false}
                    />
                </Col>
            </Row>

            <Row xs="auto">
                <Col xs={1}></Col>
                <Col>
                    <Form.Control
                        type="text"
                        placeholder="Value"
                        disabled={operator === Operator.BT ? false : true}
                    />
                </Col>
            </Row>

            <Modal size="xl" show={show} onHide={handleClose} centered>
                <Modal.Header closeButton>
                    <Modal.Title>{Messages.COMMON_SELECT_OPERATOR}</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <BasicOperatorSelector
                        onOperatorSelected={handleOperatorSelected}
                    ></BasicOperatorSelector>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                        Cancel
                    </Button>
                </Modal.Footer>
            </Modal>
        </Container>
    );
};

function getOperatorSymbol(op: Operator): [string, string] {
    let opsym = "";
    let optxt = "";
    switch (op) {
        case Operator.EQ:
            opsym = Messages.EQ;
            optxt = Messages.EQUAL_DESC;
            break;
        case Operator.NE:
            opsym = Messages.NE;
            optxt = Messages.NOT_EQUAL_DESC;
            break;
        case Operator.GT:
            opsym = Messages.GT;
            optxt = Messages.GREATER_THAN_DESC;
            break;
        case Operator.LT:
            opsym = Messages.LT;
            optxt = Messages.LESS_THAN_DESC;
            break;
        case Operator.GE:
            opsym = Messages.GE;
            optxt = Messages.GREATER_EQUAL_DESC;
            break;
        case Operator.LE:
            opsym = Messages.LE;
            optxt = Messages.LESS_EQUAL_DESC;
            break;
        case Operator.IN:
            opsym = Messages.I;
            optxt = Messages.IN_DESC;
            break;
        case Operator.NI:
            opsym = Messages.E;
            optxt = Messages.NOT_IN_DESC;
            break;
        case Operator.BT:
            opsym = Messages.BT;
            optxt = Messages.BETWEEN;
            break;
        case Operator.NB:
            opsym = Messages.NB;
            optxt = Messages.NOT_BETWEEN_DESC;
            break;
        case Operator.ANY:
            opsym = Messages.ANYVAL;
            optxt = Messages.ANY_DESC;
            break;

        default:
            break;
    }
    return [opsym, optxt];
}

export default Conditionsss;

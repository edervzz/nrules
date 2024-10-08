import { Col, Container, Row } from "react-bootstrap";
import { Operator } from "../../enums";
import BasicOperator from "../BasicOperator";
import Messages from "../../locales/Messages";

type Props = {
    onOperatorSelected: (op: Operator) => void;
};

function BasicOperatorSelector({ onOperatorSelected }: Props) {
    return (
        <Container fluid>
            <Row>
                <Col md="auto">
                    <BasicOperator
                        operator={Messages.EQ}
                        operText={Messages.EQUAL}
                        operDescription={Messages.EQUAL_DESC}
                        operEnum={Operator.EQ}
                        onClickOperator={onOperatorSelected}
                    />
                </Col>
                <Col md="auto">
                    <BasicOperator
                        operator={Messages.NE}
                        operText={Messages.NOT_EQUAL}
                        operDescription={Messages.NOT_EQUAL_DESC}
                        operEnum={Operator.NE}
                        onClickOperator={onOperatorSelected}
                    />
                </Col>

                <Col md="auto">
                    <BasicOperator
                        operator={Messages.GT}
                        operText={Messages.GREATER_THAN}
                        operDescription={Messages.GREATER_THAN_DESC}
                        operEnum={Operator.GT}
                        onClickOperator={onOperatorSelected}
                    />
                </Col>
                <Col md="auto">
                    <BasicOperator
                        operator={Messages.LT}
                        operText={Messages.LESS_THAN}
                        operDescription={Messages.LESS_THAN_DESC}
                        operEnum={Operator.LT}
                        onClickOperator={onOperatorSelected}
                    />
                </Col>
            </Row>

            <Row>
                <Col md="auto">
                    <BasicOperator
                        operator={Messages.GE}
                        operText={Messages.GREATER_EQUAL}
                        operDescription={Messages.GREATER_EQUAL_DESC}
                        operEnum={Operator.GE}
                        onClickOperator={onOperatorSelected}
                    />
                </Col>
                <Col md="auto">
                    <BasicOperator
                        operator={Messages.LE}
                        operText={Messages.LESS_EQUAL}
                        operDescription={Messages.LESS_EQUAL_DESC}
                        operEnum={Operator.LE}
                        onClickOperator={onOperatorSelected}
                    />
                </Col>

                <Col md="auto">
                    <BasicOperator
                        operator={Messages.I}
                        operText={Messages.IN}
                        operDescription={Messages.IN_DESC}
                        operEnum={Operator.IN}
                        onClickOperator={onOperatorSelected}
                    />
                </Col>
                <Col md="auto">
                    <BasicOperator
                        operator={Messages.E}
                        operText={Messages.NOT_IN}
                        operDescription={Messages.NOT_IN_DESC}
                        operEnum={Operator.NI}
                        onClickOperator={onOperatorSelected}
                    />
                </Col>
            </Row>

            <Row>
                <Col md="auto">
                    <BasicOperator
                        operator={Messages.BT}
                        operText={Messages.BETWEEN}
                        operDescription={Messages.BETWEEN_DESC}
                        operEnum={Operator.BT}
                        onClickOperator={onOperatorSelected}
                    />
                </Col>
                <Col md="auto">
                    <BasicOperator
                        operator={Messages.NB}
                        operText={Messages.NOT_BETWEEN}
                        operDescription={Messages.NOT_BETWEEN_DESC}
                        operEnum={Operator.NB}
                        onClickOperator={onOperatorSelected}
                    />
                </Col>
                <Col md="auto">
                    <BasicOperator
                        operator={Messages.ANYVAL}
                        operText={Messages.ANY}
                        operDescription={Messages.ANY_DESC}
                        operEnum={Operator.ANY}
                        onClickOperator={onOperatorSelected}
                    />
                </Col>
            </Row>
        </Container>
    );
}

export default BasicOperatorSelector;

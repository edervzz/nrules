import { NewRuleCondition, NewRuleOutput } from "../../../typings";
import { Col, Container, Row, Spinner } from "react-bootstrap";

interface Props {
    rulename: string;
    ruletype: number;
    conditions: NewRuleCondition[];
    outputs: NewRuleOutput[];
}

function Step04({}: Props) {
    return (
        <>
            <br />
            <Container>
                <Row className="justify-content-md-center">
                    <Col md="auto">
                        <Spinner animation="border" />
                    </Col>
                </Row>
            </Container>
        </>
    );
}

export default Step04;

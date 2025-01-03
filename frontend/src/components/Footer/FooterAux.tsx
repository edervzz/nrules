import { Container, Row, Col } from "react-bootstrap";

type Props = {};

function FooterAux({}: Props) {
    return (
        <>
            <Container fluid="xxl">
                <Row>
                    <Col>
                        <hr></hr>
                    </Col>
                </Row>
            </Container>
        </>
    );
}

export default FooterAux;

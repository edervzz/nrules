import { Container, Row, Col, Image } from "react-bootstrap";

function Footer() {
    return (
        <>
            <hr></hr>
            <Container style={{ width: "100%" }}>
                <Row>
                    <Col>
                        <Image height={110} src="/concredito.png" rounded />
                    </Col>
                    <Col>
                        <Image height={110} src="/yastas.png" rounded />
                    </Col>
                    <Col>
                        <Image height={110} src="/aterna.png" rounded />
                    </Col>
                    <Col>
                        <Image height={110} src="/gentera.png" rounded />
                    </Col>
                    <Col>
                        <Image height={110} src="/compartamos.png" rounded />
                    </Col>
                    <Col>
                        <Image height={110} src="/fundacion.png" rounded />
                    </Col>
                    <Col>
                        <Image height={110} src="/financiera.png" rounded />
                    </Col>
                </Row>
            </Container>
        </>
    );
}

export default Footer;

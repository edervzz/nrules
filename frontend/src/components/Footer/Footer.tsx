import { Container, Row, Col, Image } from "react-bootstrap";

type Props = {};

function Footer({}: Props) {
    return (
        <>
            <Container fluid="xxl">
                <Row>
                    <Col>
                        <hr></hr>
                    </Col>
                </Row>

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
                    <Col className="text-center">
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
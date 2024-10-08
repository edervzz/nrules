import { Col, Container, Row, Image, Badge } from "react-bootstrap";
import Menu from "../components/Menu";

export default function Home() {
    return (
        <>
            <Menu></Menu>
            <Container>
                <Row className="justify-content-md-center">
                    <Col xs lg="2">
                        <h5>Version 0.0.1</h5>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <p style={{ fontSize: "50px", fontWeight: "bold" }}>
                            NRule
                        </p>
                        <p style={{ fontSize: "50px" }}>
                            Motor de Reglas ágil creado por y para
                            <br />
                            <Image src="/gentera-logo.png" rounded />
                        </p>
                    </Col>
                    <Col>
                        <p>Capacidades</p>
                        <ul>
                            <li>Multi Empresa</li>
                            <li>Flujos de Trabajo</li>
                            <li>Tablas de Decisión</li>
                            <li>Árboles de Decisión</li>
                            <li>Transporte de Cambios</li>
                            <li>Ambientes: DEV-TEST-PROD</li>
                        </ul>

                        <p>Tecnología</p>
                        <ul>
                            <li>Arquitectura Clean</li>
                            <li>CQRS disponible</li>
                            <li>Contenerizado</li>
                            <li>React</li>
                            <li>Python</li>
                        </ul>
                    </Col>
                </Row>
            </Container>
        </>
    );
}

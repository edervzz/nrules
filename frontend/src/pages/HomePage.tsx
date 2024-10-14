import { Col, Container, Row, Image, Badge } from "react-bootstrap";
import Menubar from "../components/Menubar";
import Footer from "./Footer";

export default function HomePage() {
    return (
        <>
            <Menubar></Menubar>

            <Container>
                <Row></Row>
                <Row>
                    <Col sm="1"></Col>
                    <Col md="6">
                        <p style={{ fontSize: "80px" }}>
                            NRule{" "}
                            <Badge
                                style={{
                                    fontSize: "20px",
                                }}
                                bg="success"
                            >
                                v0.0.1
                            </Badge>
                        </p>
                        <p style={{ fontSize: "38px", fontWeight: "bold" }}>
                            Un Motor de Reglas diseñado en productos actuales
                            del mercado
                        </p>
                        <p style={{ fontSize: "30px" }}>
                            NRule le ayuda en los procesos diarios de servicios
                            financieros, seguros, logística y más.
                        </p>
                        <br />
                    </Col>
                    <Col sm="1"></Col>
                    <Col md="3">
                        <br />
                        <br />
                        <p style={{ fontSize: "20px" }}>Capacidades Actuales</p>
                        <ul>
                            <li>Tablas de Decisión</li>
                            <li>Multi Empresa</li>
                            <li>Transporte de Cambios</li>
                            <li>Despliegues: Dev-Test-Prod</li>
                        </ul>
                        <p style={{ fontSize: "20px" }}>
                            Especificación Técnica
                        </p>
                        <ul>
                            <li>Clean Architecture</li>
                            <li>Containers</li>
                            <li>Open-Api</li>
                            <li>Python</li>
                            <li>React</li>
                            <li>Typescript</li>
                            <li>Bootstrap</li>
                        </ul>
                    </Col>
                    <Col sm="1"></Col>
                </Row>
                <Row>
                    <Col sm="1"></Col>
                    <Col>
                        <p>Noticias</p>
                        <ul>
                            <li>
                                Proximamente se lanzará nueva funcionalidad para
                                creación de Árboles de Decisión.
                            </li>
                            <li>
                                Runner ya esta disponible para uso por API en
                                los ambientes de DEV-TEST-PROD.
                            </li>
                            <li>
                                Runner ya esta disponible en el ambiente DEV en
                                su versión Visual.
                            </li>
                        </ul>
                    </Col>
                    <Col sm="1"></Col>
                </Row>
            </Container>

            <Footer></Footer>
        </>
    );
}

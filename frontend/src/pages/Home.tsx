import { Col, Container, Row, Image, Badge } from "react-bootstrap";
import Menu from "../components/Menu";

export default function Home() {
    return (
        <>
            <Menu></Menu>

            <Container>
                <Row></Row>
                <Row>
                    <Col sm="1"></Col>
                    <Col md="6">
                        <p style={{ fontSize: "50px" }}>
                            NRule{" "}
                            <Badge style={{ fontSize: "20px" }} bg="success">
                                v0.0.1
                            </Badge>
                        </p>
                        <p style={{ fontSize: "35px", fontWeight: "bold" }}>
                            Motor de Reglas diseñado en productos actuales del
                            mercado
                        </p>
                        <p style={{ fontSize: "25px" }}>
                            NRule le ayuda en los procesos diarios de servicios
                            financieros, seguros, logística y más.
                        </p>
                        <br />
                        <Image height={305} src="/gentera-logo.png" rounded />
                    </Col>

                    <Col sm="4">
                        <p>Capacidades</p>
                        <ul>
                            <li>Tablas de Decisión</li>
                            <li>Multi Empresa</li>
                            <li>Transporte de Cambios</li>
                            <li>Despliegues: Dev-Test-Prod</li>
                        </ul>
                        <br />
                        <p>Especificación Backend</p>
                        <ul>
                            <li>Arquitectura Clean</li>
                            <li>Contenerizado</li>
                            <li>Telemetria</li>
                            <li>Open-Api</li>
                            <li>Python</li>
                        </ul>
                        <br />
                        <p>Especificación Frontend</p>
                        <ul>
                            <li>React</li>
                            <li>Typescript</li>
                            <li>Bootstrap</li>
                        </ul>
                        <br />
                        <p>Última versión 0.0.1</p>
                        <ul>
                            <li>Crear Tablas de Decisión</li>
                            <li>Mantenimiento Tablas de Decisión</li>
                            <li>Configuración de Ambientes y Empresas</li>
                            <li>Transporte de Cambios</li>
                        </ul>
                    </Col>
                    <Col sm="1"></Col>
                </Row>
            </Container>
        </>
    );
}

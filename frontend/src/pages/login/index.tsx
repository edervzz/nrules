import { Badge, Col, Container, Row } from "react-bootstrap";
import Login from "./Login";
import Footer from "../../components/Footer/Footer";
import { useState } from "react";
import { Loading01 } from "../../components/Loading";
import Messages from "../../locales/Messages";
import MainContainer from "../../components/MainContainer";

export default function LoginPage() {
    const [showLoad, setShowLoad] = useState(false);
    const [isFailure, setIsFailure] = useState(false);
    const [messageError, setMessageError] = useState("");

    const handleTryConnecting = () => {
        setIsFailure(false);
        setShowLoad(true);
    };
    const handleFailureConnection = (merr: string) => {
        setIsFailure(true);
        setMessageError(merr);
    };

    const handleClose = () => {
        setShowLoad(false);
    };

    return (
        <MainContainer isLoginPage>
            {showLoad && (
                <Loading01
                    title={Messages.CONNECTING}
                    isFailure={isFailure}
                    messageOnFailure={messageError}
                    onClose={handleClose}
                ></Loading01>
            )}
            <Container fluid="xl" className=" justify-content-center">
                <Row>
                    <Col></Col>
                    <Col sm="6">
                        <p style={{ fontSize: "60px" }}>
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
                            {Messages.NRULE_INFO}
                        </p>
                        <p style={{ fontSize: "30px" }}>
                            {Messages.NRULE_HELP}
                        </p>
                    </Col>
                    <Col>
                        <br></br>
                        <Login
                            onTryConnecting={handleTryConnecting}
                            onFailureConnection={handleFailureConnection}
                        ></Login>
                    </Col>
                    <Col></Col>
                </Row>
                <Row>
                    <Col></Col>
                    <Col sm="3" className="text-start">
                        <p style={{ fontSize: "20px" }}>
                            {Messages.NRULE_SPECS}
                        </p>
                        <ul>
                            <li>Clean Architecture</li>
                            <li>Open-API</li>
                            <li>Python</li>
                            <li>React, Bootstrap</li>
                        </ul>
                    </Col>
                    <Col sm="3">
                        <p style={{ fontSize: "20px" }}>
                            {Messages.NRULE_CAPABILITIES}
                        </p>
                        <ul>
                            <li>Tablas de Decisión</li>
                            <li>Multi Empresa</li>
                            <li>Transporte de Cambios</li>
                            <li>Despliegues: Dev-Test-Prod</li>
                        </ul>
                    </Col>
                    <Col></Col>
                    <Col></Col>
                </Row>
            </Container>
            <Footer></Footer>
        </MainContainer>
    );
}

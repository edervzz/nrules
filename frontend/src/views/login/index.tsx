import { Badge, Col, Container, Row } from "react-bootstrap";
import Login from "../../components/Login";
import Footer from "../../components/Footer/Footer";
import { useState } from "react";
import { LoadingModal } from "../../components/LoadingModal";
import Messages from "../../locales/Messages";
import Session from "../../components/Session";

export default function LoginView() {
    const [showLoadingModal, setShowLoadingModal] = useState(false);
    const [isFailure, setIsFailure] = useState(false);
    const [messageError, setMessageError] = useState("");

    const handleTryConnecting = () => {
        setIsFailure(false);
        setShowLoadingModal(true);
    };
    const handleFailureConnection = (merr: string) => {
        setIsFailure(true);
        setMessageError(merr);
    };

    const handleClose = () => {
        setShowLoadingModal(false);
    };

    return (
        <Session isLoginPage>
            <LoadingModal
                show={showLoadingModal}
                title={Messages.MESSAGE_CONNECTING}
                isFailure={isFailure}
                messageOnFailure={messageError}
                onClose={handleClose}
            ></LoadingModal>
            <Container fluid="xl" className=" justify-content-center">
                <Row>
                    <Col></Col>
                    <Col sm="6">
                        <p style={{ fontSize: "60px" }}>
                            {Messages.NRULE + " "}
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
                            <li>Árboles de Decisión</li>
                            <li>Tablas de Decisión</li>
                            <li>Multi Empresa</li>
                            <li>Transporte de Cambios</li>
                        </ul>
                    </Col>
                    <Col></Col>
                    <Col></Col>
                </Row>
            </Container>
            <Footer></Footer>
        </Session>
    );
}

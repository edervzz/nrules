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
            {/* conditional renders */}
            {showLoadingModal && (
                <LoadingModal
                    title={Messages.MESSAGE_CONNECTING}
                    isFailure={isFailure}
                    messageOnFailure={messageError}
                    onClose={handleClose}
                />
            )}

            <Container fluid="sm" className="mt-3">
                <Row>
                    <Col xl="8" style={{ backgroundColor: "" }}>
                        <p style={{ fontSize: "60px" }}>
                            {Messages.KITE + " "}
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
                            {Messages.KITE_HELP}
                        </p>
                    </Col>
                    <Col
                        className="d-flex justify-content-center"
                        style={{ backgroundColor: "" }}
                    >
                        <Login
                            onTryConnecting={handleTryConnecting}
                            onFailureConnection={handleFailureConnection}
                        ></Login>
                    </Col>
                </Row>
                <Row>
                    <br></br>
                </Row>
                <Row>
                    <Col xl="3"></Col>
                    <Col xl="3">
                        <p style={{ fontSize: "20px" }}>
                            {Messages.KITE_SPECS}
                        </p>
                        <ul>
                            <li>Clean Architecture</li>
                            <li>Open-API</li>
                            <li>Python</li>
                            <li>React, Bootstrap</li>
                        </ul>
                    </Col>
                    <Col xl="3">
                        <p style={{ fontSize: "20px" }}>
                            {Messages.KITE_CAPABILITIES}
                        </p>
                        <ul>
                            <li>Decision Trees</li>
                            <li>Decision Tables</li>
                            <li>Multi-tenancy</li>
                            <li>Transports</li>
                        </ul>
                    </Col>
                    <Col xl="3"></Col>
                </Row>
                <div
                    style={{
                        position: "fixed",
                        left: 0,
                        bottom: 0,
                        width: "100%",
                        textAlign: "center",
                    }}
                >
                    <Footer></Footer>
                </div>
            </Container>
        </Session>
    );
}

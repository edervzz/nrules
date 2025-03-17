import { Col, Container, Modal, Row, Spinner } from "react-bootstrap";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import Messages from "../../locales/Messages";
import styles from "./MainMenu.module.css";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import EnvarsSession from "../../envars";

interface Props {
    link_tables?: string;
    brand?: string;
    title?: string;
    fluid?: boolean | string | "sm" | "md" | "lg" | "xl" | "xxl";
}

export default function Menubar({ fluid = "xxl", brand, title }: Props) {
    const [showLogout, setShowLogout] = useState(false);
    const navigate = useNavigate();

    const tenantData = EnvarsSession.tenant;
    if (tenantData.id == 0) return <></>;

    const handleClickLogout = () => {
        EnvarsSession.clear();
        setShowLogout(true);
        navigate("/");
    };

    return (
        <>
            {showLogout && (
                <Modal size="lg" show={true} backdrop="static">
                    <Modal.Header closeButton>
                        <Modal.Title>{Messages.MENUBAR_LOGING_OUT}</Modal.Title>
                    </Modal.Header>

                    <Modal.Body>
                        <Container>
                            <Row className="justify-content-md-center">
                                <Col md="auto">
                                    <Spinner animation="border" />
                                </Col>
                            </Row>
                        </Container>
                    </Modal.Body>
                </Modal>
            )}

            {/* <Nav.Link className={styles.link} href="/rules">
                {brand}
            </Nav.Link> */}

            <Navbar expand="md" className={`bg-body-tertiary`}>
                <Container fluid={fluid}>
                    <Navbar.Brand>{title}</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto"></Nav>
                    </Navbar.Collapse>

                    <Navbar.Collapse
                        className="justify-content-end"
                        id="basic-navbar-nav"
                    >
                        <Nav>
                            <Nav.Link className={styles.link} href="/rules">
                                {Messages.MENUBAR_RULES}
                            </Nav.Link>
                            <Nav.Link className={styles.link} href="/runner">
                                {Messages.MENUBAR_RUNNER}
                            </Nav.Link>
                            <Nav.Link
                                className={styles.link}
                                href="/transports"
                            >
                                {Messages.MENUBAR_TRANSPORTS}
                            </Nav.Link>

                            <NavDropdown
                                title={
                                    <>
                                        <i className="bi bi-stack" />{" "}
                                        {tenantData.id +
                                            " - " +
                                            tenantData.tenantName}
                                    </>
                                }
                            >
                                <NavDropdown.ItemText>
                                    {tenantData.tenantName}
                                </NavDropdown.ItemText>
                                <NavDropdown.ItemText>
                                    <i className="bi bi-person-circle" />{" "}
                                    {tenantData.username}
                                </NavDropdown.ItemText>

                                <NavDropdown.Divider />
                                <NavDropdown.Item
                                    className={styles.link}
                                    onClick={handleClickLogout}
                                >
                                    <i className="bi bi-box-arrow-right"></i>{" "}
                                    {Messages.MENUBAR_SIGN_OUT}
                                </NavDropdown.Item>
                            </NavDropdown>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    );
}

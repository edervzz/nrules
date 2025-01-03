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
    link_new?: string;
    onClickNew?: () => void;
    link_tables?: string;
    title?: string;
}

export default function Menubar({
    link_new = "/new",
    onClickNew,
    title,
}: Props) {
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

            <Navbar expand="md" className={`bg-body-tertiary`}>
                <Container fluid="xxl">
                    <Navbar.Brand>{title}</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto">
                            <Nav.Link
                                className={styles.link}
                                href={link_new}
                                onClick={() => onClickNew?.()}
                            >
                                {Messages.MENUBAR_NEW_RULE}
                            </Nav.Link>

                            <NavDropdown title={Messages.MENUBAR_RULES}>
                                <Nav.Link
                                    className={styles.link}
                                    href="/matrix"
                                >
                                    {Messages.MENUBAR_MATRIXES}
                                </Nav.Link>
                            </NavDropdown>

                            <NavDropdown title={<>{Messages.MENUBAR_GO}</>}>
                                <Nav.Link
                                    className={styles.link}
                                    href="/runner"
                                >
                                    {Messages.MENUBAR_RUNNER}
                                </Nav.Link>
                                <NavDropdown.Divider />

                                <NavDropdown.Item
                                    className={styles.link}
                                    href="/transports"
                                >
                                    {Messages.MENUBAR_TRANSPORTS}
                                </NavDropdown.Item>
                                <NavDropdown.Item
                                    className={styles.link}
                                    href="/tenancy"
                                >
                                    {Messages.MENUBAR_TENANTS}
                                </NavDropdown.Item>
                            </NavDropdown>
                        </Nav>
                    </Navbar.Collapse>

                    <Navbar.Collapse
                        className="justify-content-end"
                        id="basic-navbar-nav"
                    >
                        <Nav>
                            <NavDropdown
                                title={
                                    <>
                                        <i className="bi bi-building-fill" />
                                        {tenantData.tenantName}
                                    </>
                                }
                            >
                                <NavDropdown.ItemText>
                                    <i className="bi bi-person-circle" />{" "}
                                    {tenantData.username}
                                </NavDropdown.ItemText>
                                <NavDropdown.ItemText>
                                    TID: {tenantData.id}
                                </NavDropdown.ItemText>

                                <NavDropdown.Divider />
                                <NavDropdown.Item
                                    className={styles.link}
                                    onClick={handleClickLogout}
                                >
                                    <i className="bi bi-box-arrow-right"></i>
                                    {" " + Messages.MENUBAR_SIGN_OUT}
                                </NavDropdown.Item>
                            </NavDropdown>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    );
}

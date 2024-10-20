// import { useState } from "react";
import { Col, Container, Modal, Row, Spinner } from "react-bootstrap";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import Messages from "../../locales/Messages";
import styles from "./MainMenu.module.css";
import { useState } from "react";

import { TenantDto } from "../../typings";
import { useNavigate } from "react-router-dom";
import Vars from "../../vars";

interface Props {
    link_new?: string;
    onClickNew?: () => void;
    link_tables?: string;
}

export default function Menubar({ link_new = "/new", onClickNew }: Props) {
    const [showLogout, setShowLogout] = useState(false);
    const navigate = useNavigate();

    const tenantData = Vars.tenant;
    if (tenantData == null) return <></>;
    const tenant = JSON.parse(tenantData) as TenantDto;

    const handleClickLogout = () => {
        Vars.clear();
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
                <Container fluid="xl">
                    <Navbar.Text></Navbar.Text>
                    <Navbar.Brand href="/home">NRule</Navbar.Brand>
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

                            <Nav.Link className={styles.link} href="/tables">
                                {Messages.MENUBAR_MATRIXES}
                            </Nav.Link>

                            <Nav.Link className={styles.link} href="/runner">
                                {Messages.MENUBAR_RUNNER}
                            </Nav.Link>

                            <NavDropdown
                                title={Messages.MENUBAR_MANAGEMENT}
                                id="basic-nav-dropdown"
                            >
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
                        <NavDropdown
                            title={
                                <>
                                    <i className="bi bi-building-fill" />
                                    {tenant.tenantName}
                                </>
                            }
                            id="basic-nav-dropdown"
                        >
                            <NavDropdown.ItemText>
                                <i className="bi bi-person-circle" />{" "}
                                {tenant.username}
                            </NavDropdown.ItemText>
                            <NavDropdown.ItemText>
                                TID: {tenant.id}
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
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    );
}

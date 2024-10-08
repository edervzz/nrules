// import { useState } from "react";
import { Badge, Container } from "react-bootstrap";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";

import Messages from "../../locales/Messages";
import styles from "./MainMenu.module.css";
import i18next from "i18next";

type Props = {
    link_new?: string;
    onClickNew?: () => void;
    link_tables?: string;
};

function Menu({ link_new = "/new", onClickNew = () => {} }: Props) {
    const navDropdownTitle = (
        <>
            <i className="bi bi-person-circle" />
            {" master"}
        </>
    );

    return (
        <>
            {/* Navigation Bar*/}
            <Navbar expand="md" className={`bg-body-tertiary`}>
                <Container>
                    <Navbar.Text></Navbar.Text>
                    <Navbar.Brand href="/">NRule</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto">
                            <Nav.Link
                                className={styles.link}
                                href={link_new}
                                onClick={() => onClickNew()}
                            >
                                {Messages.NEW_RULE}
                            </Nav.Link>
                            <Nav.Link className={styles.link} href="/tables">
                                {Messages.TABLES}
                            </Nav.Link>

                            <NavDropdown
                                title={Messages.MANAGEMENT}
                                id="basic-nav-dropdown"
                            >
                                <NavDropdown.Item
                                    className={styles.link}
                                    href="/transports"
                                >
                                    {Messages.TRANSPORTS}
                                </NavDropdown.Item>
                                <NavDropdown.Item
                                    className={styles.link}
                                    href="/tenancy"
                                >
                                    {Messages.TENANTS}
                                </NavDropdown.Item>
                            </NavDropdown>
                        </Nav>
                    </Navbar.Collapse>

                    <Navbar.Collapse
                        className="justify-content-end"
                        id="basic-navbar-nav"
                    >
                        <NavDropdown
                            title={navDropdownTitle}
                            id="basic-nav-dropdown"
                        >
                            <NavDropdown.ItemText>
                                <Badge bg="success">v0.0.1</Badge>
                            </NavDropdown.ItemText>

                            <NavDropdown.Item
                                className={styles.link}
                                onClick={() => i18next.changeLanguage("en")}
                            ></NavDropdown.Item>

                            <NavDropdown.Item
                                className={styles.link}
                                href="#action/3.1"
                            >
                                {Messages.SETTINGS}
                            </NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item
                                className={styles.link}
                                href="#action/3.4"
                            >
                                <i className="bi bi-box-arrow-right"></i>
                                {" " + Messages.SIGN_OUT}
                            </NavDropdown.Item>
                        </NavDropdown>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    );
}

export default Menu;

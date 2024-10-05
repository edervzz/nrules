import { useState } from "react";
import { Container } from "react-bootstrap";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import NewRule from "../NewRule";
import Messages from "../../locales/Messages";
import styles from "./MainMenu.module.css";

function MainMenu() {
    const [showNewRule, setShowNewRule] = useState(false);

    const handleShowNewRule = () => {
        setShowNewRule(true);
    };
    const handleHideNewRule = () => {
        setShowNewRule(false);
    };

    const navDropdownTitle = (
        <>
            <i className="bi bi-person-circle" />
            {" osvelazquez"}
        </>
    );

    return (
        <>
            {/* show modal - New Rule */}
            {showNewRule && <NewRule onHide={handleHideNewRule} />}

            {/* Navigation Bar*/}
            <Navbar expand="md" className={`bg-body-tertiary`}>
                <Container>
                    <Navbar.Brand href="#home">NRule</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto">
                            <Nav.Link
                                className={styles.link}
                                onClick={() => handleShowNewRule()}
                            >
                                {Messages.NEW_RULE}
                            </Nav.Link>
                            <Nav.Link className={styles.link} href="#tables">
                                {Messages.TABLES}
                            </Nav.Link>

                            <Nav.Link className={styles.link} href="#trees">
                                {Messages.TREES}
                            </Nav.Link>

                            <NavDropdown
                                title={Messages.MANAGEMENT}
                                id="basic-nav-dropdown"
                            >
                                <NavDropdown.Item
                                    className={styles.link}
                                    href="#action/3.1"
                                >
                                    {Messages.TRANSPORTS}
                                </NavDropdown.Item>
                                <NavDropdown.Item
                                    className={styles.link}
                                    href="#action/3.2"
                                >
                                    {Messages.TENANTS}
                                </NavDropdown.Item>
                                <NavDropdown.Divider />
                                <NavDropdown.Item
                                    className={styles.link}
                                    href="#action/3.4"
                                >
                                    {Messages.USERS}
                                </NavDropdown.Item>
                            </NavDropdown>
                        </Nav>
                    </Navbar.Collapse>

                    <Navbar.Collapse className="justify-content-end">
                        <NavDropdown
                            title={navDropdownTitle}
                            id="basic-nav-dropdown"
                        >
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

export default MainMenu;

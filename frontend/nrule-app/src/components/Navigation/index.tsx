import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import { Button, Container } from "react-bootstrap";
import NewRule from "../NewRule";
import Messages from "../../locales/Messages";
import { useState } from "react";

function Navigation() {
    const [show, setShow] = useState(false);
    const handleClick = () => {
        setShow(true);
    };
    const handleHide = () => {
        setShow(false);
    };
    return (
        <>
            {/* show modal - New Rule */}
            {show && <NewRule onHide={handleHide} />}

            {/* Navigation Bar*/}
            <Navbar expand="md" className={`bg-body-tertiary`}>
                <Container>
                    <Navbar.Brand href="#home">NRule</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto">
                            <Nav.Link
                                onClick={() => handleClick()}
                                style={{
                                    color: "white",
                                    backgroundColor: "#0d6efd",
                                    borderRadius: "10px",
                                }}
                            >
                                {Messages.NEW_RULE}
                            </Nav.Link>
                            <Nav.Link href="#tables">
                                {Messages.TABLES}
                            </Nav.Link>

                            <Nav.Link href="#trees">{Messages.TREES}</Nav.Link>
                            <Nav.Link href="#flows">{Messages.FLOWS}</Nav.Link>
                            <NavDropdown
                                title={Messages.MANAGEMENT}
                                id="basic-nav-dropdown"
                            >
                                <NavDropdown.Item href="#action/3.1">
                                    {Messages.TRANSPORTS}
                                </NavDropdown.Item>
                                <NavDropdown.Item href="#action/3.2">
                                    {Messages.TENANTS}
                                </NavDropdown.Item>
                                <NavDropdown.Divider />
                                <NavDropdown.Item href="#action/3.4">
                                    {Messages.USERS}
                                </NavDropdown.Item>
                            </NavDropdown>
                        </Nav>
                    </Navbar.Collapse>
                    <Navbar.Collapse className="justify-content-end">
                        <Navbar.Text>
                            Signed in as:{" "}
                            <a href="#login">osvelazquez@compartamos.com</a>
                        </Navbar.Text>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    );
}

export default Navigation;

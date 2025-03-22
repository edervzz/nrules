import {
    Button,
    Col,
    Container,
    Modal,
    Row,
    Spinner,
    Form,
    InputGroup,
    DropdownButton,
    Dropdown,
} from "react-bootstrap";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import Messages from "../../locales/Messages";
import { ReactNode, useState } from "react";
import { useNavigate } from "react-router-dom";
import EnvarsSession from "../../envars";
import { Pagination } from "../../typings";

interface Props {
    fluid?: boolean | string | "sm" | "md" | "lg" | "xl" | "xxl";
    brand?: string;
    title?: string;
    isPaginated?: boolean;
    pagination?: Pagination;
    isSearchable?: boolean;
    onSearch?: (nextPage: number, word: string) => void;
    extraItems?: ReactNode[];
}

export default function Menubar({
    fluid = "xxl",
    brand,
    title,
    isPaginated = false,
    pagination,
    isSearchable = false,
    onSearch,
    extraItems,
}: Props) {
    const [wordToSearch, setWordToSearch] = useState("");
    const [showLogout, setShowLogout] = useState(false);
    const navigate = useNavigate();

    const pageSize = pagination?.pageSize || 0;
    const currentPageNo = pagination?.currentPageNo || 0;
    const totalCount = pagination?.totalCount || 0;

    const from = pageSize * currentPageNo - pageSize + 1;
    const to =
        pageSize * currentPageNo > totalCount
            ? totalCount
            : pageSize * currentPageNo;

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

            <Navbar className={`bg-body-tertiary`}>
                <Container fluid={fluid}>
                    <Navbar.Brand>{brand}</Navbar.Brand>

                    <Nav className="me-auto">
                        <Nav.Link href="/rules">
                            {Messages.MENUBAR_RULES}
                        </Nav.Link>
                        <Nav.Link href="/runner">
                            {Messages.MENUBAR_RUNNER}
                        </Nav.Link>
                        <Nav.Link href="/transports">
                            {Messages.MENUBAR_TRANSPORTS}
                        </Nav.Link>
                    </Nav>

                    {isSearchable && (
                        <InputGroup style={{ width: "200px" }} className="me-3">
                            <Form.Control
                                value={wordToSearch}
                                onChange={(e) => {
                                    setWordToSearch(e.currentTarget.value);
                                }}
                                name="search"
                                placeholder={Messages.TOOLBAR_SEARCH}
                                aria-label="search"
                                aria-describedby="basic-addon1"
                                size="sm"
                            />
                            <Button
                                onClick={() => {
                                    onSearch!(1, wordToSearch);
                                }}
                                size="sm"
                                variant="secondary"
                            >
                                <i className="bi bi-search"></i>
                            </Button>
                        </InputGroup>
                    )}

                    {isPaginated && (
                        <>
                            <NavDropdown
                                id="dropdown-basic-button"
                                className="me-3"
                                title={
                                    from.toString() +
                                    "-" +
                                    to.toString() +
                                    " " +
                                    Messages.COMMON_OF +
                                    " " +
                                    pagination?.totalCount.toString()
                                }
                            >
                                <NavDropdown.Item
                                    disabled={
                                        (pagination?.prevPageNo || 0) == 0
                                    }
                                    onClick={() => onSearch?.(1, wordToSearch)}
                                >
                                    {Messages.BUTTON_FIRST}
                                </NavDropdown.Item>
                                <NavDropdown.Item
                                    disabled={
                                        (pagination?.nextPageNo || 0) == 0
                                    }
                                    onClick={() =>
                                        onSearch?.(
                                            pagination?.totalPages || 0,
                                            wordToSearch
                                        )
                                    }
                                >
                                    {Messages.BUTTON_LAST}
                                </NavDropdown.Item>
                            </NavDropdown>

                            <Nav.Link
                                className="me-2"
                                disabled={(pagination?.prevPageNo || 0) == 0}
                                onClick={() =>
                                    onSearch?.(
                                        pagination?.prevPageNo || 0,
                                        wordToSearch
                                    )
                                }
                            >
                                <i className="bi bi-chevron-left"></i>
                            </Nav.Link>

                            <Nav.Link
                                className="me-2"
                                disabled={(pagination?.nextPageNo || 0) == 0}
                                onClick={() =>
                                    onSearch?.(
                                        pagination?.nextPageNo || 0,
                                        wordToSearch
                                    )
                                }
                            >
                                <i className="bi bi-chevron-right"></i>
                            </Nav.Link>

                            {/* <Button
                                className="me-1"
                                disabled={(pagination?.prevPageNo || 0) == 0}
                                onClick={() =>
                                    onSearch?.(
                                        pagination?.prevPageNo || 0,
                                        wordToSearch
                                    )
                                }
                                size="sm"
                                variant="primary"
                            >
                                <i className="bi bi-chevron-left"></i>
                            </Button>
                            <Button
                                className="me-3"
                                disabled={(pagination?.nextPageNo || 0) == 0}
                                onClick={() =>
                                    onSearch?.(
                                        pagination?.nextPageNo || 0,
                                        wordToSearch
                                    )
                                }
                                size="sm"
                                variant="primary"
                            >
                                <i className="bi bi-chevron-right"></i>
                            </Button> */}
                        </>
                    )}

                    {/* tenant info */}
                    <Nav>
                        <NavDropdown
                            title={
                                <>
                                    <i className="bi bi-stack" />{" "}
                                    {tenantData.id}
                                </>
                            }
                        >
                            <NavDropdown.ItemText>
                                <i className="bi bi-building"></i>{" "}
                                {tenantData.tenantName}
                            </NavDropdown.ItemText>
                            <NavDropdown.ItemText>
                                <i className="bi bi-person-circle" />{" "}
                                {tenantData.username}
                            </NavDropdown.ItemText>

                            <NavDropdown.Divider />
                            <NavDropdown.Item onClick={handleClickLogout}>
                                <i className="bi bi-box-arrow-right"></i>{" "}
                                {Messages.MENUBAR_SIGN_OUT}
                            </NavDropdown.Item>
                        </NavDropdown>
                    </Nav>
                </Container>
            </Navbar>
        </>
    );
}

import { ReactNode, useState } from "react";
import {
    Button,
    Col,
    Container,
    Dropdown,
    DropdownButton,
    Form,
    InputGroup,
    OverlayTrigger,
    Row,
    Tooltip,
} from "react-bootstrap";
import Messages from "../../locales/Messages";
import { Pagination } from "../../typings";

interface Props {
    fluid?: boolean | string | "sm" | "md" | "lg" | "xl" | "xxl";
    title?: string;
    titleInfo?: ReactNode;
    isPaginated?: boolean;
    pagination?: Pagination;

    isSearchable?: boolean;
    onSearch?: (nextPage: number, word: string) => void;
    extraItems?: ReactNode[];
}

function Toolbar({
    fluid = "xxl",
    title,
    titleInfo,
    isPaginated = false,
    pagination,
    isSearchable = false,
    onSearch,
    extraItems,
}: Props) {
    const [wordToSearch, setWordToSearch] = useState("");
    const pageSize = pagination?.pageSize || 0;
    const currentPageNo = pagination?.currentPageNo || 0;
    const totalCount = pagination?.totalCount || 0;

    const from = pageSize * currentPageNo - pageSize + 1;
    const to =
        pageSize * currentPageNo > totalCount
            ? totalCount
            : pageSize * currentPageNo;
    return (
        <>
            <Container
                fluid={fluid}
                className="mb-1"
                style={{ backgroundColor: "white" }}
            >
                <Row className="align-items-center">
                    {title && (
                        <Col xs="auto" className="fs-5">
                            {title}
                            <span className="fs-5">
                                {titleInfo && (
                                    <OverlayTrigger
                                        placement="bottom"
                                        delay={{ show: 250, hide: 400 }}
                                        overlay={(props) => {
                                            return (
                                                <Tooltip
                                                    id="button-tooltip"
                                                    {...props}
                                                >
                                                    {titleInfo}
                                                </Tooltip>
                                            );
                                        }}
                                    >
                                        <i className="bi bi-info-circle-fill ms-2"></i>
                                    </OverlayTrigger>
                                )}
                            </span>
                        </Col>
                    )}

                    {extraItems?.map((x, idx) => (
                        <Col xs="auto" key={"extra-" + idx}>
                            {x}
                        </Col>
                    ))}

                    {isSearchable && (
                        <>
                            <Col></Col>
                            <Col xs="4">
                                <InputGroup>
                                    <Form.Control
                                        value={wordToSearch}
                                        onChange={(e) => {
                                            setWordToSearch(
                                                e.currentTarget.value
                                            );
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
                                        variant="primary"
                                    >
                                        <i className="bi bi-search"></i>
                                    </Button>
                                </InputGroup>
                            </Col>
                            <Col></Col>
                        </>
                    )}

                    {isPaginated && (
                        <Col xs="auto" className="text-end">
                            <Row className="align-items-center row-cols-auto">
                                <Col>
                                    <DropdownButton
                                        id="dropdown-basic-button"
                                        variant="light"
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
                                        <Dropdown.Item
                                            disabled={
                                                (pagination?.prevPageNo || 0) ==
                                                0
                                            }
                                            onClick={() =>
                                                onSearch?.(1, wordToSearch)
                                            }
                                        >
                                            {Messages.BUTTON_FIRST}
                                        </Dropdown.Item>
                                        <Dropdown.Item
                                            disabled={
                                                (pagination?.nextPageNo || 0) ==
                                                0
                                            }
                                            onClick={() =>
                                                onSearch?.(
                                                    pagination?.totalPages || 0,
                                                    wordToSearch
                                                )
                                            }
                                        >
                                            {Messages.BUTTON_LAST}
                                        </Dropdown.Item>
                                    </DropdownButton>
                                </Col>
                                <Col style={{ margin: 0, padding: 0 }}>
                                    <Button
                                        disabled={
                                            (pagination?.prevPageNo || 0) == 0
                                        }
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
                                        className="ms-1 me-3"
                                        disabled={
                                            (pagination?.nextPageNo || 0) == 0
                                        }
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
                                    </Button>
                                </Col>
                            </Row>
                        </Col>
                    )}
                </Row>
            </Container>
        </>
    );
}

export default Toolbar;

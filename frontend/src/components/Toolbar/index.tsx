import { ReactNode, useState } from "react";
import {
    Button,
    Col,
    Container,
    Form,
    InputGroup,
    OverlayTrigger,
    Row,
    Tooltip,
} from "react-bootstrap";
import Paginator from "../Paginator";
import { Pagination } from "../../typings";

interface Props {
    fluid?: boolean | string | "sm" | "md" | "lg" | "xl" | "xxl";
    title?: string;
    titleInfo?: ReactNode;
    isPaginated?: boolean;
    pagination?: Pagination;
    onGotoPage?: (nextPage: number, word: string) => void;
    isSearchable?: boolean;
    onSearch?: (word: string) => void;
    extraItems?: ReactNode[];
}

const Toolbar = ({
    fluid = "xxl",
    title,
    titleInfo,
    isPaginated = false,
    pagination,
    onGotoPage,
    isSearchable = false,
    onSearch,
    extraItems,
}: Props) => {
    const [wordToSearch, setWordToSearch] = useState("");
    return (
        <>
            <Container fluid={fluid} className="mb-1 mt-1">
                <Row className="align-items-center">
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

                    {extraItems?.map((x) => (
                        <Col xs="auto" key={x?.toString()}>
                            {x}
                        </Col>
                    ))}

                    <Col></Col>

                    {isSearchable && (
                        <Col xs="3">
                            <InputGroup>
                                <Form.Control
                                    value={wordToSearch}
                                    onChange={(e) => {
                                        setWordToSearch(e.currentTarget.value);
                                    }}
                                    name="search"
                                    placeholder="busqueda"
                                    aria-label="buscar"
                                    aria-describedby="basic-addon1"
                                />
                                <Button
                                    onClick={() => {
                                        onSearch!(wordToSearch);
                                    }}
                                    size="sm"
                                    variant="primary"
                                >
                                    <i className="bi bi-search"></i>
                                </Button>
                            </InputGroup>
                        </Col>
                    )}

                    {isPaginated && (
                        <Col xs="auto" className="text-end">
                            <Paginator
                                pagination={pagination!}
                                onGotoPage={(nextPage) =>
                                    onGotoPage!(nextPage, wordToSearch)
                                }
                            />
                        </Col>
                    )}
                </Row>
            </Container>
        </>
    );
};

export default Toolbar;

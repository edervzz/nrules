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
import { Pagination } from "../../typings";
import Paginator from "../Paginator";

interface Props {
    title: string;
    titleInfo?: ReactNode;
    action01Icon?: string; // e.g. bi-arrow-clockwise
    onAction01?: () => void;
    action02Icon?: string; // e.g. bi-arrow-clockwise
    onAction02?: () => void;
    action03Icon?: string; // e.g. bi-arrow-clockwise
    onAction03?: () => void;
    isPaginated?: boolean;
    pagination?: Pagination;
    onGotoPage?: (nextPage: number) => void;
    isSearchable?: boolean;
    onSearch?: (word: string) => void;
    buttons?: ReactNode[];
}

const Toolbar = ({
    title,
    titleInfo,
    action01Icon,
    onAction01,
    action02Icon,
    onAction02,
    action03Icon,
    onAction03,
    isPaginated = false,
    pagination,
    onGotoPage: onGotoPage,
    isSearchable = false,
    onSearch,
    buttons,
}: Props) => {
    const [wordToSearch, setWordToSearch] = useState("");
    return (
        <>
            <Container className="mb-2 mt-2">
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
                    <Col>
                        {onAction01 != undefined && (
                            <Button
                                onClick={() => {
                                    onAction01();
                                }}
                                className="me-1"
                                size="sm"
                                variant="primary"
                            >
                                <i className={"bi " + action01Icon}></i>
                            </Button>
                        )}
                        {onAction02 != undefined && (
                            <Button
                                onClick={() => {
                                    onAction02();
                                }}
                                className="me-1"
                                size="sm"
                                variant="primary"
                            >
                                <i className={"bi " + action02Icon}></i>
                            </Button>
                        )}
                        {onAction03 != undefined && (
                            <Button
                                onClick={() => {
                                    onAction03();
                                }}
                                className="me-1"
                                size="sm"
                                variant="primary"
                            >
                                <i className={"bi " + action03Icon}></i>
                            </Button>
                        )}
                        {buttons?.map((x) => x)}
                    </Col>

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
                                onGotoPage={onGotoPage!}
                            />
                        </Col>
                    )}
                </Row>
            </Container>
        </>
    );
};

export default Toolbar;

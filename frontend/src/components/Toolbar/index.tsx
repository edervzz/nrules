import { ReactNode } from "react";
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
    hideSearch?: boolean;
}

const Toolbar = ({
    title,
    titleInfo,
    action01Icon,
    onAction01,
    isPaginated = false,
    pagination,
    onGotoPage: onGotoPage,
    hideSearch = false,
}: Props) => {
    const from =
        (pagination?.pageSize || 0) * (pagination?.currentPageNo || 0) -
        (pagination?.pageSize || 0) +
        1;
    let to = (pagination?.pageSize || 0) * (pagination?.currentPageNo || 0);
    if (to > (pagination?.totalCount || 0)) {
        to = pagination?.totalCount || 0;
    }
    return (
        <Container className="mb-2 mt-2">
            <Row className="align-items-center">
                <Col sm="3" className="fs-3">
                    {title}
                    <span className="fs-5">
                        {titleInfo && (
                            <OverlayTrigger
                                placement="bottom"
                                delay={{ show: 250, hide: 400 }}
                                overlay={(props) => {
                                    return (
                                        <Tooltip id="button-tooltip" {...props}>
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
                </Col>

                <Col sm="3">
                    {!hideSearch && (
                        <InputGroup>
                            <Form.Control
                                name="search"
                                placeholder="busqueda"
                                aria-label="buscar"
                                aria-describedby="basic-addon1"
                            />
                            <Button size="sm" variant="secondary">
                                <i className="bi bi-search"></i>
                            </Button>
                        </InputGroup>
                    )}
                </Col>
                {isPaginated && (
                    <Col sm="3" className="text-end">
                        {from.toString() +
                            " - " +
                            to.toString() +
                            " Total " +
                            pagination?.totalCount.toString()}
                        <Button
                            disabled={pagination?.prevPageNo == 0}
                            onClick={() => onGotoPage?.(1)}
                            className="ms-3 me-1"
                            size="sm"
                            variant="secondary"
                        >
                            <i className="bi bi-chevron-bar-left"></i>
                        </Button>
                        <Button
                            disabled={(pagination?.prevPageNo || 0) == 0}
                            onClick={() =>
                                onGotoPage?.(pagination?.prevPageNo || 0)
                            }
                            className="me-1"
                            size="sm"
                            variant="secondary"
                        >
                            <i className="bi bi-chevron-compact-left"></i>
                        </Button>
                        <Button
                            disabled={(pagination?.nextPageNo || 0) == 0}
                            onClick={() =>
                                onGotoPage?.(pagination?.nextPageNo || 0)
                            }
                            className="me-1"
                            size="sm"
                            variant="secondary"
                        >
                            <i className="bi bi-chevron-compact-right"></i>
                        </Button>
                        <Button
                            disabled={pagination?.nextPageNo == 0}
                            onClick={() =>
                                onGotoPage?.(pagination?.totalPages || 0)
                            }
                            className="me-1"
                            size="sm"
                            variant="secondary"
                        >
                            <i className="bi bi-chevron-bar-right"></i>
                        </Button>
                    </Col>
                )}
            </Row>
        </Container>
    );
};

export default Toolbar;

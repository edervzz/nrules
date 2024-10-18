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

interface Pagination {
    from: number;
    to: number;
    total: number;
}

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
    hideSearch?: boolean;
}

const Toolbar = ({
    title,
    titleInfo,
    action01Icon,
    onAction01,
    isPaginated = false,
    pagination,
    hideSearch = false,
}: Props) => {
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
                        {pagination?.from}-{pagination?.to} Total{" "}
                        {pagination?.total}
                        <Button
                            disabled
                            className="ms-3 me-1"
                            size="sm"
                            variant="secondary"
                        >
                            <i className="bi bi-chevron-bar-left"></i>
                        </Button>
                        <Button className="me-1" size="sm" variant="secondary">
                            <i className="bi bi-chevron-compact-left"></i>
                        </Button>
                        <Button className="me-1" size="sm" variant="secondary">
                            <i className="bi bi-chevron-compact-right"></i>
                        </Button>
                        <Button className="me-1" size="sm" variant="secondary">
                            <i className="bi bi-chevron-bar-right"></i>
                        </Button>
                    </Col>
                )}
            </Row>
        </Container>
    );
};

export default Toolbar;

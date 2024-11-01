import { Button, Col, Dropdown, DropdownButton, Row } from "react-bootstrap";

import Messages from "../../locales/Messages";
import { Pagination } from "../../typings";

interface Props {
    pagination?: Pagination;
    onGotoPage?: (nextPage: number) => void;
}

function Paginator({ pagination, onGotoPage }: Props) {
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
                            disabled={(pagination?.prevPageNo || 0) == 0}
                            onClick={() => onGotoPage?.(1)}
                        >
                            {Messages.BUTTON_FIRST}
                        </Dropdown.Item>
                        <Dropdown.Item
                            disabled={(pagination?.nextPageNo || 0) == 0}
                            onClick={() =>
                                onGotoPage?.(pagination?.totalPages || 0)
                            }
                        >
                            {Messages.BUTTON_LAST}
                        </Dropdown.Item>
                    </DropdownButton>
                </Col>
                <Col style={{ margin: 0, padding: 0 }}>
                    <Button
                        disabled={(pagination?.prevPageNo || 0) == 0}
                        onClick={() =>
                            onGotoPage?.(pagination?.prevPageNo || 0)
                        }
                        size="sm"
                        variant="primary"
                    >
                        <i className="bi bi-chevron-left"></i>
                    </Button>

                    <Button
                        className="ms-1"
                        disabled={(pagination?.nextPageNo || 0) == 0}
                        onClick={() =>
                            onGotoPage?.(pagination?.nextPageNo || 0)
                        }
                        size="sm"
                        variant="primary"
                    >
                        <i className="bi bi-chevron-right"></i>
                    </Button>
                </Col>
            </Row>
        </>
    );
}

export default Paginator;

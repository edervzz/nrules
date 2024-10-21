import { useEffect, useState } from "react";
import {
    Container,
    Form,
    Row,
    Table,
    Toast,
    ToastContainer,
} from "react-bootstrap";
import { Pagination, RuleDto, TenantDto } from "../../typings";
import axios, { AxiosError } from "axios";
import Toolbar from "../../components/Toolbar";
import Messages from "../../locales/Messages";
import { READ_RULES_PAGE } from "../../api";
import Vars from "../../vars";

interface Props {}

function Matrixes({}: Props) {
    const pageSize = 10;
    const [localPagination, setLocalPagination] = useState<Pagination>({
        currentPageNo: 0,
        nextPageNo: 0,
        prevPageNo: 0,
        pageSize: pageSize,
        totalPages: 0,
        totalCount: 0,
    });
    const [rules, setRules] = useState<RuleDto[]>([]);
    const [showInfoMessage, setShowInfoMessage] = useState(false);
    const [showErrorMessage, setShowErrorMessage] = useState(false);
    const [messageError, setMessageError] = useState("");

    const handleAction01 = () => {
        callApiGetRules(1);
    };

    const handleGotoPage = (nextPage: number) => {
        callApiGetRules(nextPage);
    };

    const callApiGetRules = (pageNo: number) => {
        setShowInfoMessage(true);
        setShowErrorMessage(false);
        setMessageError(Messages.MESSAGE_LOADING);
        setRules([]);

        const tenant = Vars.tenant;
        const tenantDto = JSON.parse(tenant) as TenantDto;

        axios
            .get<RuleDto[]>(
                READ_RULES_PAGE(
                    tenantDto.id.toString(),
                    pageNo.toString(),
                    pageSize.toString()
                )
            )
            .then((res) => {
                setShowInfoMessage(false);
                setRules(res.data);
                const nextPage = res.headers["next-page"];
                const prevPage = res.headers["previous-page"];
                const totalPages = res.headers["total-pages"];
                const totalCount = res.headers["total-count"];

                setLocalPagination({
                    nextPageNo: nextPage,
                    prevPageNo: prevPage,
                    pageSize: localPagination.pageSize,
                    currentPageNo: pageNo,
                    totalPages: totalPages,
                    totalCount: totalCount,
                });
            })
            .catch(function (error: AxiosError) {
                setShowErrorMessage(true);
                setShowInfoMessage(false);
                setMessageError(error.message);
            });
    };

    useEffect(() => {
        handleAction01();
    }, []);

    return (
        <>
            {/* Error */}
            <ToastContainer position="top-center" style={{ zIndex: 1 }}>
                <Toast
                    onClose={() => setShowErrorMessage(false)}
                    show={showErrorMessage}
                    delay={2000}
                    autohide
                    bg="danger"
                >
                    <Toast.Body className={"text-white text-center"}>
                        {messageError}
                    </Toast.Body>
                </Toast>
            </ToastContainer>
            {/* Information */}
            <ToastContainer position="top-center" style={{ zIndex: 1 }}>
                <Toast
                    onClose={() => setShowInfoMessage(false)}
                    show={showInfoMessage}
                    delay={20000}
                    autohide
                    bg="secondary"
                >
                    <Toast.Body className="text-white text-center">
                        {Messages.MESSAGE_LOADING}
                    </Toast.Body>
                </Toast>
            </ToastContainer>

            <Toolbar
                title={Messages.COMMON_MATRIX}
                isPaginated
                pagination={localPagination}
                onAction01={handleAction01}
                action01Icon="bi-arrow-clockwise"
                onGotoPage={handleGotoPage}
            ></Toolbar>

            <Container>
                <Row>
                    <Table striped bordered hover>
                        <thead>
                            <tr>
                                <th style={{ width: "0rem" }}>
                                    <Form.Check
                                        name="masterCheck"
                                        checked
                                        onChange={() => {}}
                                    />
                                </th>
                                <th>Regla</th>
                                <th>Estrategia</th>
                                <th>Dev</th>
                                <th>Test</th>
                                <th>Prod</th>

                                <th className="text-center">Estado</th>
                            </tr>
                        </thead>
                        <tbody>
                            {rules.map((x) => (
                                <tr key={x.id}>
                                    <td>
                                        <Form.Check
                                            name={x.id}
                                            onChange={() => {}}
                                        />
                                    </td>
                                    <td>{x.name}</td>
                                    <td>{x.strategy}</td>
                                    <td>{x.version}</td>
                                    <td>{x.version}</td>
                                    <td>{x.version}</td>
                                    <td className="text-center">
                                        <i
                                            className="bi bi-check-circle-fill"
                                            style={{ color: "green" }}
                                        ></i>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </Table>
                </Row>
            </Container>

            {/* <Container>
                <Row
                    className="align-items-center"
                    style={{ paddingBottom: "10px", paddingTop: "10px" }}
                >
                    <Col></Col>
                    <Col className="text-end">
                        20-40 de 1500
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
                </Row>
            </Container> */}
        </>
    );
}

export default Matrixes;

import { useEffect, useState } from "react";
import {
    Button,
    Container,
    OverlayTrigger,
    Row,
    Table,
    Toast,
    ToastContainer,
    Tooltip,
} from "react-bootstrap";
import { Pagination, ReadRuleDto } from "../../typings";
import Toolbar from "../../components/Toolbar";
import Messages from "../../locales/Messages";
import Vars from "../../vars";
import { GetRulesPaged } from "../../adapters/RuleAdapter";

interface Props {}

function Matrixes({}: Props) {
    const pageSize = 15;
    const [rules, setRules] = useState<ReadRuleDto[]>([]);
    const [showInfoMessage, setShowInfoMessage] = useState(false);
    const [showErrorMessage, setShowErrorMessage] = useState(false);
    const [messageError, setMessageError] = useState("");
    const [wordToSearch, setWordToSearch] = useState("");
    const [localPagination, setLocalPagination] = useState<Pagination>({
        currentPageNo: 1,
        nextPageNo: 0,
        prevPageNo: 0,
        pageSize: pageSize,
        totalPages: 0,
        totalCount: 0,
    });

    const handleGotoPage = (nextPage: number) => {
        callApiGetRules(nextPage, wordToSearch);
    };

    const handleSearch = (word: string) => {
        setWordToSearch(word);
        setLocalPagination({
            currentPageNo: 1,
            nextPageNo: 0,
            prevPageNo: 0,
            pageSize: pageSize,
            totalPages: 0,
            totalCount: 0,
        });
        callApiGetRules(1, word);
    };

    const callApiGetRules = (pageNo: number, word: string) => {
        setShowInfoMessage(true);
        setShowErrorMessage(false);
        setMessageError(Messages.MESSAGE_LOADING);
        setRules([]);

        GetRulesPaged(pageNo, pageSize, word).then((result) => {
            if (result.ok) {
                setShowInfoMessage(false);
                setRules(result.data!);
                setLocalPagination({
                    nextPageNo: result.nextPage,
                    prevPageNo: result.prevPage,
                    pageSize: localPagination.pageSize,
                    currentPageNo: pageNo,
                    totalPages: result.totalPages,
                    totalCount: result.totalCount,
                });
            } else {
                setShowErrorMessage(true);
                setShowInfoMessage(false);
                setMessageError(result.errorMessage || "");
            }
        });
    };

    useEffect(() => {
        callApiGetRules(localPagination.currentPageNo, wordToSearch);
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
                titleInfo={Messages.MATRIX_INFO}
                isSearchable
                isPaginated
                pagination={localPagination}
                onGotoPage={handleGotoPage}
                onSearch={handleSearch}
            ></Toolbar>

            <Container fluid="xxl">
                <Row>
                    <Table striped bordered hover>
                        <thead>
                            <tr>
                                <th>{Messages.NEWRULE_RULENAME}</th>
                                <th>{Messages.NEWRULE_RULESTRATEGY}</th>
                                <th>Default Output</th>
                                <th>Dev</th>
                                <th>Test</th>
                                <th>Prod</th>
                                <th className="text-center">
                                    {Messages.NEWRULE_STATUS}
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            {rules.map((x) => (
                                <tr
                                    key={x.id}
                                    style={{
                                        fontSize: "14px",
                                        fontWeight: "bold",
                                        color: "#868686",
                                    }}
                                >
                                    <td>
                                        <a
                                            style={{
                                                fontSize: "14px",
                                                fontWeight: "bold",
                                                textTransform: "uppercase",
                                                textDecoration: "none",
                                                color: "#0d6efd",
                                            }}
                                            href={"/editor/" + x.id}
                                        >
                                            {x.name}
                                        </a>
                                    </td>
                                    <td>{x.strategy}</td>
                                    <td>
                                        {x.default_kvs ? (
                                            <i
                                                className="bi bi-check-circle-fill"
                                                style={{ color: "green" }}
                                            ></i>
                                        ) : (
                                            <i
                                                className="bi bi-x-circle-fill"
                                                style={{ color: "gray" }}
                                            ></i>
                                        )}
                                    </td>
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
        </>
    );
}

export default Matrixes;

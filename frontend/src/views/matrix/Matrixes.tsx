import { useEffect, useState } from "react";
import { Container, Row, Table, Toast, ToastContainer } from "react-bootstrap";
import { ReadRuleDto } from "../../models";
import Toolbar from "../../components/Toolbar";
import Messages from "../../locales/Messages";
import Storage from "../../storage";
import { Pagination } from "../../typings";
import { ToastError, ToastLoading } from "../../components/Toasts";

interface Props {}

function Matrixes({}: Props) {
    const pageSize = 15;
    const [rules, setRules] = useState<ReadRuleDto[]>([]);
    const [showToast, setShowToast] = useState(0);
    const [localPagination, setLocalPagination] = useState<Pagination>({
        currentPageNo: 1,
        nextPageNo: 0,
        prevPageNo: 0,
        pageSize: pageSize,
        totalPages: 0,
        totalCount: 0,
    });

    const callApiGetRules = (pageNo: number, word: string) => {
        setShowToast(1);
        setRules([]);

        Storage.Rule.GetRulesPaged(pageNo, pageSize, word).then((result) => {
            if (result.ok) {
                setShowToast(0);
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
                setShowToast(2);
            }
        });
    };

    useEffect(() => {
        callApiGetRules(localPagination.currentPageNo, "");
    }, []);

    return (
        <>
            {showToast == 1 && <ToastLoading></ToastLoading>}
            {showToast == 2 && <ToastError></ToastError>}

            {/* Toolbar */}
            <Toolbar
                // title={Messages.COMMON_MATRIX}
                // titleInfo={Messages.MATRIX_INFO}
                isSearchable
                isPaginated
                pagination={localPagination}
                onGotoPage={(nextPage, word) => callApiGetRules(nextPage, word)}
                onSearch={(word) => callApiGetRules(1, word)}
            ></Toolbar>

            {/* Main */}
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

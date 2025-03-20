import { useEffect, useState } from "react";
import { RuleDto } from "../../models";

import Session from "../../components/Session";
import Menubar from "../../components/Menubar";
import Storage from "../../storage";
import Footer from "../../components/Footer/Footer";
import { Pagination } from "../../typings";
import Messages from "../../locales/Messages";
import Toolbar from "../../components/Toolbar";
import { ToastError, ToastLoading } from "../../components/Toasts";
import Board from "../../components/Board";
import { Button, Nav } from "react-bootstrap";

export default function RulesView() {
    // 1. States
    const [rules, setRules] = useState<RuleDto[]>([]);
    const [showToast, setShowToast] = useState(0);
    const [pagination, setPagination] = useState<Pagination>({
        currentPageNo: 1,
        nextPageNo: 0,
        prevPageNo: 0,
        pageSize: 15,
        totalPages: 0,
        totalCount: 0,
    });
    // 2. handlers
    const handleSearch = (pageNo: number, word: string) => {
        setShowToast(1);
        setRules([]);

        Storage.Rule.GetRulesPaged(pageNo, pagination.pageSize, word).then(
            (result) => {
                if (result.ok) {
                    setShowToast(0);
                    setRules(result.data!);
                    setPagination({
                        nextPageNo: result.nextPage,
                        prevPageNo: result.prevPage,
                        pageSize: pagination.pageSize,
                        currentPageNo: pageNo,
                        totalPages: result.totalPages,
                        totalCount: result.totalCount,
                    });
                } else {
                    setShowToast(2);
                }
            }
        );
    };
    // 3.Effects
    useEffect(() => {
        handleSearch(pagination.currentPageNo, "");
    }, []);

    return (
        <Session>
            {showToast == 1 && <ToastLoading />}
            {showToast == 2 && <ToastError />}

            <Menubar
                brand={Messages.NRULE}
                title={Messages.MENUBAR_RULES}
                isPaginated
                pagination={pagination}
                isSearchable
                onSearch={(nextPage, word) => handleSearch(nextPage, word)}
                extraItems={[
                    <Nav.Link key={1} href="/new">
                        <i id="pencil" className="bi bi-pencil me-2" />
                        {Messages.MENUBAR_NEW_RULE}
                    </Nav.Link>,
                ]}
            />

            <Board rules={rules} />
            <div
                style={{
                    position: "fixed",
                    left: 0,
                    bottom: 0,
                    width: "100%",
                    textAlign: "center",
                }}
            >
                <Footer></Footer>
            </div>
        </Session>
    );
}

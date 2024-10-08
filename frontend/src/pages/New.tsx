import { useState } from "react";
import Menu from "../components/Menu";
import NewRule from "../components/NewRule";

export default function New() {
    const [showNewRule, setShowNewRule] = useState(true);

    const handleHideNewRule = () => {
        setShowNewRule(false);
    };

    const handleShowNewRule = () => {
        setShowNewRule(true);
    };

    return (
        <>
            <Menu link_new="#" onClickNew={handleShowNewRule} />
            {showNewRule && <NewRule onHide={handleHideNewRule} />}
        </>
    );
}

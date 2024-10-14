import { useState } from "react";
import Menubar from "../components/Menubar";
import NewRule from "../components/NewRule";

export default function NewPage() {
    const [showNewRule, setShowNewRule] = useState(true);

    const handleHideNewRule = () => {
        setShowNewRule(false);
    };

    const handleShowNewRule = () => {
        setShowNewRule(true);
    };

    return (
        <>
            <Menubar link_new="#" onClickNew={handleShowNewRule} />
            {showNewRule && <NewRule onHide={handleHideNewRule} />}
        </>
    );
}

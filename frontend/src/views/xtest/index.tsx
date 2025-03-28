import { useState } from "react";
import Footer from "../../components/Footer/Footer";
import Menubar from "../../components/Menubar";
import Operator from "../../components/Operator";

function XTest() {
    const [show, setShow] = useState(true);

    const handleSubmit = (name: string, type: string) => {
        setShow(false);
    };
    const handleCancel = () => {
        setShow(false);
    };

    return (
        <>
            <Menubar brand="NRule"></Menubar>

            <Footer></Footer>
        </>
    );
}

export default XTest;

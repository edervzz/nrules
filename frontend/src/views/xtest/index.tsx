import { useState } from "react";
import Footer from "../../components/Footer/Footer";
import Menubar from "../../components/Menubar";
import Condition from "../../components/Condition";
import Operator from "../../components/Operator";

function XTest() {
    const [show, setShow] = useState(true);

    const handleSubmit = (name: string, type: string) => {
        console.log(name, type);

        setShow(false);
    };
    const handleCancel = () => {
        setShow(false);
    };

    return (
        <>
            <Menubar brand="NRule"></Menubar>
            {show && <Operator></Operator>}
            <Footer></Footer>
        </>
    );
}

export default XTest;

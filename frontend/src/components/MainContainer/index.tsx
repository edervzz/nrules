import { ReactNode, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Session from "../../session";

interface Props {
    children: ReactNode;
    isLoginPage?: boolean;
}

export default function MainContainer({ children, isLoginPage }: Props) {
    const [show, setShow] = useState(false);
    const navigate = useNavigate();

    const validateLogin = () => {
        const tenantData = Session.tenant;
        if (isLoginPage) {
            if (tenantData == null) {
                setShow(true);
            } else {
                navigate("/home");
            }
        } else {
            if (tenantData == null) {
                navigate("/");
            } else {
                setShow(true);
                return;
            }
        }
    };

    useEffect(() => {
        validateLogin();
    }, []);

    return show && children;
}

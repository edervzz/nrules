import { ReactNode, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import EnvarsSession from "../../envars";

interface Props {
    children: ReactNode;
    isLoginPage?: boolean;
}

/**
 * Main Container to wrap any children (React Node) to validate if a user is logged
 * @param children React Node to show
 * @param isLoginPage set if current url path is the login page
 * @returns children
 */
export default function Session({ children, isLoginPage }: Props) {
    const navigate = useNavigate();

    const validate = () => {
        const tenantData = EnvarsSession.tenant;
        if (isLoginPage) {
            if (tenantData.id != 0) {
                navigate("/rules");
            }
        } else {
            if (tenantData == null || tenantData.id == 0) {
                navigate("/");
            }
        }
    };

    useEffect(() => {
        validate();
    }, []);

    return children;
}

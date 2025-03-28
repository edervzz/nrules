import { FormEvent, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { changeLocale } from "../../locales/i18n";
import { TenantDto } from "../../models";
import Messages from "../../locales/Messages";
import EnvarsSession, { EnvarsLocal } from "../../envars";

interface Props {
    onTryConnecting: () => void;
    onFailureConnection: (messageError: string) => void;
}

export default function Login({ onTryConnecting, onFailureConnection }: Props) {
    const [langu, setLangu] = useState(EnvarsLocal.language);
    const tidRef = useRef<HTMLInputElement>(null);
    const usernameRef = useRef<HTMLInputElement>(null);
    const passwordRef = useRef<HTMLInputElement>(null);
    const navigate = useNavigate();

    const call_api = async () => {
        onTryConnecting();
        const delay = (ms: number) => new Promise((res) => setTimeout(res, ms));
        await delay(2000);
        if (
            parseInt(tidRef.current?.value!) === 101 &&
            usernameRef.current?.value === "osvelazquez" &&
            passwordRef.current?.value === "1234"
        ) {
            const tenant: TenantDto = {
                id: 101,
                tenantName: "Compartamos Banco",
                tokenDev: "1234567890",
                tokenTest: "1234567890",
                tokenProd: "1234567890",
                username: usernameRef.current?.value,
            };
            EnvarsSession.tenant = tenant;
            navigate("/rules");
        } else {
            onFailureConnection(Messages.MESSAGE_ERROR_USR_PWD);
        }
    };

    const handleSubmit = (event: FormEvent) => {
        event.preventDefault();
        call_api();
    };

    return (
        <div className="card" style={{ width: "250px" }}>
            <div className="card-body">
                <form className="text-end" onSubmit={handleSubmit}>
                    <div className="card-title text-start">
                        {Messages.LOGIN_LOGIN}
                    </div>
                    <div className="card-text">
                        <select
                            className="form-select mb-2"
                            value={langu}
                            onChange={(v) => {
                                setLangu(v.currentTarget.value);
                                changeLocale(v.currentTarget.value);
                                window.location.reload();
                            }}
                        >
                            <option value="es">🇲🇽-Español</option>
                            <option value="en">🇺🇸-English</option>
                        </select>

                        <input
                            className="form-control mb-2"
                            placeholder={Messages.LOGIN_TENANTID}
                            aria-describedby="basic-addon1"
                            ref={tidRef}
                        />
                        <input
                            className="form-control mb-2"
                            placeholder={Messages.LOGIN_USERNAME}
                            aria-label="Username"
                            aria-describedby="basic-addon1"
                            ref={usernameRef}
                        />
                        <input
                            className="form-control mb-2"
                            placeholder={Messages.LOGIN_PASSWORD}
                            type="password"
                            id="inputPassword5"
                            aria-describedby="passwordHelpBlock"
                            ref={passwordRef}
                        />
                    </div>

                    <div className="d-grid">
                        <button type="submit" className="btn btn-primary">
                            {Messages.BUTTON_CONTINUE}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}

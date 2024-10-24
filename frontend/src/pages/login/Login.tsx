import { Button, Card, Container, Form } from "react-bootstrap";
import Messages from "../../locales/Messages";
import { useNavigate } from "react-router-dom";
import { FormEvent, useRef, useState } from "react";
import { changeLocale } from "../../locales/i18n";
import { TenantDto } from "../../typings";
import Vars from "../../vars";

interface Props {
    onTryConnecting: () => void;
    onFailureConnection: (messageError: string) => void;
}

export default function Login({ onTryConnecting, onFailureConnection }: Props) {
    const [langu, setLangu] = useState(Vars.language);

    const languRef = useRef<HTMLSelectElement>(null);
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
            Vars.tenant = tenant;
            navigate("/home");
        } else {
            onFailureConnection(Messages.MESSAGE_ERROR_USR_PWD);
        }
    };

    const handleSubmit = (event: FormEvent) => {
        event.preventDefault();
        call_api();
    };

    return (
        <Form onSubmit={handleSubmit}>
            <Card style={{ width: "18rem" }}>
                <Card.Body>
                    <Card.Title>{Messages.LOGIN_LOGIN}</Card.Title>
                    <Card.Text>
                        <Form.Select
                            className="mb-2"
                            ref={languRef}
                            value={langu}
                            onChange={(v) => {
                                setLangu(v.currentTarget.value);
                                changeLocale(v.currentTarget.value);
                                window.location.reload();
                            }}
                        >
                            <option value="es">🇲🇽-Español</option>
                            <option value="en">🇺🇸-English</option>
                        </Form.Select>

                        <Form.Control
                            className="mb-2"
                            placeholder={Messages.LOGIN_TENANTID}
                            aria-describedby="basic-addon1"
                            ref={tidRef}
                        />
                        <Form.Control
                            className="mb-2"
                            placeholder={Messages.LOGIN_USERNAME}
                            aria-label="Username"
                            aria-describedby="basic-addon1"
                            ref={usernameRef}
                        />
                        <Form.Control
                            placeholder={Messages.LOGIN_PASSWORD}
                            type="password"
                            id="inputPassword5"
                            aria-describedby="passwordHelpBlock"
                            ref={passwordRef}
                        />
                    </Card.Text>
                    <Container
                        fluid="xl"
                        className="d-flex align-items-center justify-content-end"
                    >
                        <Button variant="primary" type="submit">
                            {Messages.BUTTON_CONTINUE}
                        </Button>
                    </Container>
                </Card.Body>
            </Card>
        </Form>
    );
}

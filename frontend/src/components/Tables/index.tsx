import { useEffect, useState } from "react";
import { Container, Form, Row, Table, Toast } from "react-bootstrap";
import { RuleDto } from "../../typings";
import axios from "axios";
import Toolbar from "../Toolbar";

type Props = {};

function Tables({}: Props) {
    const [rules, setRules] = useState<RuleDto[]>([]);

    const reload = () => {
        setRules([]);
        axios
            .get<RuleDto[]>(
                "http://localhost:5000/nr/api/v1/t/105/rules?pageNo=1&pageSize=20"
            )
            .then((res) => {
                setRules(res.data);
            });
    };

    useEffect(() => {
        reload();
    }, []);

    return (
        <>
            <Toolbar
                title="Tablas de Decisión"
                pagination
                action01={reload}
                action01Icon="bi-arrow-clockwise"
            ></Toolbar>

            <Container>
                <Row>
                    <Table striped bordered hover>
                        <thead>
                            <tr>
                                <th style={{ width: "0rem" }}>
                                    <Form.Check checked onChange={() => {}} />
                                </th>
                                <th>Regla</th>
                                <th>Estrategia</th>
                                <th>Dev</th>
                                <th>Test</th>
                                <th>Prod</th>

                                <th className="text-center">Estado</th>
                            </tr>
                        </thead>
                        <tbody>
                            {rules.map((x) => (
                                <tr key={x.id}>
                                    <td>
                                        <Form.Check onChange={() => {}} />
                                    </td>
                                    <td>{x.name}</td>
                                    <td>{x.strategy}</td>
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

            {/* <Container>
                <Row
                    className="align-items-center"
                    style={{ paddingBottom: "10px", paddingTop: "10px" }}
                >
                    <Col></Col>
                    <Col className="text-end">
                        20-40 de 1500
                        <Button
                            disabled
                            className="ms-3 me-1"
                            size="sm"
                            variant="secondary"
                        >
                            <i className="bi bi-chevron-bar-left"></i>
                        </Button>
                        <Button className="me-1" size="sm" variant="secondary">
                            <i className="bi bi-chevron-compact-left"></i>
                        </Button>
                        <Button className="me-1" size="sm" variant="secondary">
                            <i className="bi bi-chevron-compact-right"></i>
                        </Button>
                        <Button className="me-1" size="sm" variant="secondary">
                            <i className="bi bi-chevron-bar-right"></i>
                        </Button>
                    </Col>
                </Row>
            </Container> */}
        </>
    );
}

export default Tables;

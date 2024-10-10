import { Button, Col, Container, Form, Row, Table } from "react-bootstrap";

type Props = {};

function Tables({}: Props) {
    return (
        <Container>
            <Row
                className="align-items-center"
                style={{ paddingBottom: "10px", paddingTop: "10px" }}
            >
                <Col sm="3">Tablas de Decisión</Col>
                <Col sm="6">
                    <Form.Control placeholder="Busqueda"></Form.Control>
                </Col>
                <Col sm="2" className="text-end">
                    300-320 de 995
                </Col>
                <Col sm="1">
                    <i
                        style={{ paddingLeft: "20px" }}
                        className="bi bi-chevron-left"
                    ></i>
                    <i
                        style={{ paddingLeft: "20px" }}
                        className="bi bi-chevron-right"
                    ></i>
                </Col>
            </Row>

            <Row>
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th style={{ width: "0rem" }}>
                                <Form.Check checked />
                            </th>
                            <th>
                                <Row className="align-items-center">
                                    <Col>
                                        <Button variant="light" size="sm">
                                            <span className="bi bi-truck" />
                                            {" Transportar"}
                                        </Button>
                                    </Col>
                                    <Col></Col>
                                </Row>
                            </th>
                            <th>Estrategia</th>
                            <th>Dev</th>
                            <th>Test</th>
                            <th>Prod</th>

                            <th className="text-center">Estado</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <Form.Check // prettier-ignore
                                    type="checkbox"
                                />
                            </td>
                            <td>ru.productoComercial.oficinaServicio</td>
                            <td>EARLY</td>
                            <td>1</td>
                            <td>1</td>
                            <td>1</td>
                            <td className="text-center">
                                <i
                                    className="bi bi-check-circle-fill"
                                    style={{ color: "green" }}
                                ></i>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <Form.Check // prettier-ignore
                                    type="checkbox"
                                />
                            </td>
                            <td>ru.productoComercial.oficinaServicio</td>
                            <td>BASE</td>
                            <td>5</td>
                            <td>5</td>
                            <td>4</td>
                            <td className="text-center">
                                <i
                                    className="bi bi-exclamation-triangle-fill"
                                    style={{ color: "orange" }}
                                ></i>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <Form.Check // prettier-ignore
                                    type="checkbox"
                                />
                            </td>
                            <td>ru.productoComercial.oficinaServicio</td>
                            <td>ALL</td>
                            <td>6</td>
                            <td>5</td>
                            <td>5</td>
                            <td className="text-center">
                                <i
                                    className="bi bi-exclamation-triangle-fill"
                                    style={{ color: "orange" }}
                                ></i>
                            </td>
                        </tr>
                    </tbody>
                </Table>
            </Row>
        </Container>
    );
}

export default Tables;

import { useState } from "react";
import {
    Button,
    Col,
    Container,
    Form,
    InputGroup,
    OverlayTrigger,
    Row,
    Toast,
    Tooltip,
} from "react-bootstrap";

interface Props {
    title: string;
    pagination?: boolean;
    action01Icon?: string; // e.g. bi-arrow-clockwise
    action01?: () => void;
}

const Toolbar = ({
    title,
    pagination = false,
    action01Icon,
    action01,
}: Props) => {
    const [show, setShow] = useState(false);

    return (
        <Container className="mb-2">
            <div
                className="position-fixed top-0 start-50 translate-middle-x"
                style={{ zIndex: 11 }}
            >
                <Toast
                    onClose={() => setShow(false)}
                    show={show}
                    delay={2000}
                    autohide
                >
                    <Toast.Body>Cargando...</Toast.Body>
                </Toast>
            </div>
            <Row className="align-items-center">
                <Col>
                    {title}
                    <span className="ms-5">
                        {action01 != undefined && (
                            <Button
                                onClick={() => {
                                    setShow(true);
                                    action01();
                                }}
                                className="me-1"
                                size="sm"
                                variant="primary"
                            >
                                <i className={"bi " + action01Icon}></i>
                            </Button>
                        )}
                    </span>
                </Col>

                <Col sm="3">
                    <InputGroup>
                        <Form.Control
                            placeholder="busqueda"
                            aria-label="buscar"
                            aria-describedby="basic-addon1"
                        />
                        <Button size="sm" variant="secondary">
                            <i className="bi bi-search"></i>
                        </Button>
                    </InputGroup>
                </Col>
                {pagination && (
                    <Col sm="3" className="text-end">
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
                )}
            </Row>
        </Container>
    );
};

export default Toolbar;

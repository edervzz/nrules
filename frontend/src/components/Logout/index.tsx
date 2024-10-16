import { Col, Container, Modal, Row, Spinner } from "react-bootstrap";

interface Props {}

function Logout({}: Props) {
    return (
        <>
            <Modal size="lg" show={true} backdrop="static">
                <Modal.Header closeButton>
                    <Modal.Title>Cerrando Sesión</Modal.Title>
                </Modal.Header>

                <Modal.Body>
                    <Container>
                        <Row className="justify-content-md-center">
                            <Col md="auto">
                                <Spinner animation="border" />
                            </Col>
                        </Row>
                    </Container>
                </Modal.Body>
            </Modal>
        </>
    );
}

export default Logout;

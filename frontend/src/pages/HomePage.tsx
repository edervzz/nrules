import { Col, Container, Row, Badge } from "react-bootstrap";
import Footer from "../components/Footer/Footer";
import Menubar from "../components/Menubar";
import Messages from "../locales/Messages";
import MainContainer from "../components/MainContainer";

export default function HomePage() {
    return (
        <MainContainer>
            <Menubar></Menubar>
            <Container>
                <Row></Row>
                <Row>
                    <Col sm="1"></Col>
                    <Col md="10">
                        <p style={{ fontSize: "80px" }}>
                            NRule{" "}
                            <Badge
                                style={{
                                    fontSize: "20px",
                                }}
                                bg="success"
                            >
                                v0.0.1
                            </Badge>
                        </p>
                        <p style={{ fontSize: "28px", fontWeight: "bold" }}>
                            {Messages.NRULE_TO_START}
                        </p>
                        <br />
                    </Col>

                    <Col sm="1"></Col>
                </Row>
            </Container>
            <Footer></Footer>
        </MainContainer>
    );
}

import styles from "./Home.module.css";
import Footer from "../../components/Footer/Footer";
import Menubar from "../../components/Menubar";
import MainContainer from "../../components/MainContainer";
import Messages from "../../locales/Messages";
import { Col, Container, Row, Badge } from "react-bootstrap";

export default function HomePage() {
    return (
        <MainContainer>
            <Menubar title="NRule"></Menubar>
            <Container>
                <Row></Row>
                <Row>
                    <Col sm="1"></Col>
                    <Col md="10">
                        <p className={`${styles.logo}`}>
                            NRule{" "}
                            <Badge className={`${styles.badge}`} bg="success">
                                v0.0.1
                            </Badge>
                        </p>
                        <p className={`${styles.start}`}>
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

import styles from "./Home.module.css";
import Footer from "../../components/Footer/Footer";
import Menubar from "../../components/Menubar";
import Session from "../../components/Session";
import Messages from "../../locales/Messages";
import { Col, Container, Row } from "react-bootstrap";

export default function HomePage() {
    return (
        <Session>
            <Menubar brand="NRule"></Menubar>
            <Container>
                <Row></Row>
                <Row>
                    <Col sm="1"></Col>
                    <Col md="10">
                        <p className={`${styles.logo}`}>{Messages.NRULE}</p>
                        <p className={`${styles.start}`}>
                            {Messages.NRULE_TO_START}
                        </p>
                        <br />
                    </Col>

                    <Col sm="1"></Col>
                </Row>
            </Container>
            <Footer></Footer>
        </Session>
    );
}

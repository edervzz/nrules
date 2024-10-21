import { Container, Table } from "react-bootstrap";
import Toolbar from "../../components/Toolbar";

type Props = {};

function Editor({}: Props) {
    return (
        <>
            <Toolbar title="Editor" hideSearch></Toolbar>
            <Container fluid>
                <div className="row flex-row flex-nowrap">
                    <div className="col-3">eds</div>
                    <div className="col-3">..</div>
                    <div className="col-3">..</div>
                    <div className="col-3">..</div>
                    <div className="col-3">..</div>
                    <div className="col-3">..</div>
                    <div className="col-3">..</div>
                    <div className="col-3">..</div>
                </div>
            </Container>
        </>
    );
}

export default Editor;

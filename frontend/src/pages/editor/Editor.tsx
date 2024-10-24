import {
    Button,
    Col,
    Container,
    OverlayTrigger,
    Row,
    Table,
    Tooltip,
} from "react-bootstrap";
import Toolbar from "../../components/Toolbar";
import Vars from "../../vars";
import Messages from "../../locales/Messages";

type Props = {};

function Editor({}: Props) {
    const btnAddCondition = (
        <OverlayTrigger
            placement="top"
            delay={{ show: 150, hide: 50 }}
            overlay={<Tooltip id="tooltip">Agregar Condición</Tooltip>}
        >
            <Button
                onClick={() => {}}
                className="me-2"
                size="sm"
                variant="primary"
            >
                + <i className={"bi bi-clipboard2-check-fill"}></i>
            </Button>
        </OverlayTrigger>
    );
    const btnAddOutput = (
        <OverlayTrigger
            placement="top"
            delay={{ show: 150, hide: 50 }}
            overlay={<Tooltip id="tooltip">Agregar Resultado</Tooltip>}
        >
            <Button
                onClick={() => {}}
                className="me-2"
                size="sm"
                variant="primary"
            >
                + <i className={"bi bi-box-arrow-right"}></i>
            </Button>
        </OverlayTrigger>
    );
    return (
        <>
            <Container>
                <Row>
                    <Col>
                        {Messages.NEWRULE_RULENAME +
                            ": " +
                            Vars.ruleInProgress.name}
                    </Col>
                    <Col>
                        {Messages.NEWRULE_RULETYPE +
                            ": " +
                            Vars.ruleInProgress.rule_type}
                    </Col>
                    <Col>
                        {Messages.NEWRULE_RULESTRATEGY +
                            ": " +
                            Vars.ruleInProgress.strategy}
                    </Col>
                    <Col>{"Version" + ": " + Vars.ruleInProgress.version}</Col>
                </Row>
            </Container>
            <Toolbar
                title="Editor"
                buttons={[btnAddCondition, btnAddOutput]}
            ></Toolbar>

            <Container>
                <Table striped bordered hover responsive size="md">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Actions</th>
                            <th>Condition</th>
                            <th>Condition</th>
                            <th>Condition</th>
                            <th>Condition</th>
                            <th>Condition</th>
                            <th>Condition</th>
                            <th>Condition</th>
                            <th>Result</th>
                            <th>Result</th>
                            <th>Result</th>
                        </tr>
                    </thead>
                </Table>
            </Container>
        </>
    );
}

export default Editor;

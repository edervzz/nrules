import {
    Button,
    Container,
    OverlayTrigger,
    Table,
    Tooltip,
} from "react-bootstrap";
import Toolbar from "../../components/Toolbar";
import Vars from "../../vars";
import Messages from "../../locales/Messages";
import { useParams } from "react-router-dom";

type Props = {};

function Editor({}: Props) {
    const { id } = useParams();

    const btnAddCondition = (
        <Container>
            <OverlayTrigger
                placement="top"
                delay={{ show: 150, hide: 50 }}
                overlay={<Tooltip id="tooltip">Agregar Condición</Tooltip>}
            >
                <Button
                    name="adfas"
                    onClick={() => {}}
                    size="sm"
                    variant="primary"
                >
                    + <i className={"bi bi-clipboard2-check-fill"}></i>
                </Button>
            </OverlayTrigger>

            <OverlayTrigger
                placement="top"
                delay={{ show: 150, hide: 50 }}
                overlay={<Tooltip id="tooltip">Agregar Resultado</Tooltip>}
            >
                <Button
                    name="adfas2"
                    onClick={() => {}}
                    className="ms-1"
                    size="sm"
                    variant="primary"
                >
                    + <i className={"bi bi-box-arrow-right"}></i>
                </Button>
            </OverlayTrigger>
        </Container>
    );
    const rulename = (
        <div key={121}>
            {Messages.NEWRULE_RULENAME + ": " + Vars.ruleInProgress.name}
        </div>
    );
    const ruletype = (
        <div key={123}>
            {Messages.NEWRULE_RULETYPE + ": " + Vars.ruleInProgress.rule_type}
        </div>
    );
    const rulestrategy = (
        <div>
            {Messages.NEWRULE_RULESTRATEGY +
                ": " +
                Vars.ruleInProgress.strategy}
        </div>
    );
    return (
        <>
            <Toolbar
                fluid
                title="Editor"
                extraItems={[btnAddCondition]}
            ></Toolbar>

            <Container fluid>
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

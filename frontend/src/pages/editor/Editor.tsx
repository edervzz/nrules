import {
    Button,
    Container,
    Form,
    OverlayTrigger,
    Row,
    Table,
    Tooltip,
} from "react-bootstrap";
import Toolbar from "../../components/Toolbar";
import Vars from "../../vars";
import Messages from "../../locales/Messages";
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { GetRule } from "../../adapters/RuleAdapter";
import { ParametersDto, ReadRuleDto } from "../../typings";

type Props = {};

function Editor({}: Props) {
    const [conditions, setConditions] = useState<ParametersDto[]>([]);
    const [outputs, setOutputs] = useState<ParametersDto[]>([]);
    const [rule, setRule] = useState<ReadRuleDto>({
        id: "",
        name: "",
        rule_type: "",
        strategy: "",
        version: 0,
        default_kvs: 0,
    });
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
                    onClick={() => {
                        const oneParam = {
                            key: "qwert",
                            usefor: "CONDITION",
                            typeof: "String",
                        } as ParametersDto;
                        const newParams = [...conditions, { ...oneParam }];
                        setConditions(newParams);
                    }}
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
                    onClick={() => {
                        const oneParam = {
                            key: "qwert",
                            usefor: "OUTPUT",
                            typeof: "String",
                        } as ParametersDto;
                        const newParams = [...outputs, { ...oneParam }];
                        setOutputs(newParams);
                    }}
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

    const callGetRule = () => {
        GetRule(id || "").then((res) => {
            res.data && setRule(res.data);
            res.data &&
                setConditions(
                    res.data!.parameters?.filter(
                        (x) => x.usefor == "CONDITION"
                    ) || []
                );
            res.data &&
                setOutputs(
                    res.data!.parameters?.filter((x) => x.usefor == "OUTPUT") ||
                        []
                );
        });
    };

    useEffect(() => {
        callGetRule();
    }, []);

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
                            {conditions !== undefined &&
                                conditions!.length > 0 &&
                                conditions!.map((x) => {
                                    console.log(x);

                                    if (x.usefor == "CONDITION")
                                        return <th>Condition</th>;
                                })}

                            {outputs !== undefined &&
                                outputs!.length > 0 &&
                                outputs!.map((x) => {
                                    if (x.usefor == "OUTPUT")
                                        return <th>Result</th>;
                                })}
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td></td>
                            <td>
                                {
                                    <Container>
                                        <Form.Check
                                            type="switch"
                                            id="custom-switch"
                                        />
                                        <Button size="sm" variant="secondary">
                                            <i className="bi bi-trash3"></i>
                                        </Button>
                                    </Container>
                                }
                            </td>
                            {conditions !== undefined &&
                                conditions!.length > 0 &&
                                conditions!
                                    .filter((x) => x.usefor == "CONDITION")
                                    .map((x) => (
                                        <td>
                                            {x.key} ({x.typeof})
                                        </td>
                                    ))}

                            {outputs !== undefined &&
                                outputs!.length > 0 &&
                                outputs!
                                    .filter((x) => x.usefor == "OUTPUT")
                                    .map((x) => (
                                        <td>
                                            {x.key} ({x.typeof})
                                        </td>
                                    ))}
                        </tr>
                    </tbody>
                </Table>
            </Container>
        </>
    );
}

export default Editor;

import {
    Button,
    Col,
    Container,
    Form,
    InputGroup,
    Row,
    Table,
} from "react-bootstrap";
import Messages from "../../locales/Messages";
import {
    NewRuleCondition,
    NewRuleOutput,
    CreateRuleDto,
    ParametersDto,
    TenantDto,
    ErrorDto,
} from "../../typings";
import { ConditionType } from "../../enums";
import { FormEvent, useRef, useState } from "react";
import Toolbar from "../../components/Toolbar";
import { v4 as uuidv4 } from "uuid";
import axios, { AxiosError } from "axios";
import { CREA_RULE } from "../../api";
import Vars from "../../vars";
import { Loading02 } from "../../components/Loading";

interface Props {}

function CreateRule({}: Props) {
    const [showSending, setShowSending] = useState(false);
    const [isError, setIsError] = useState<ErrorDto[]>([]);
    const [conditions, setConditions] = useState<NewRuleCondition[]>([
        { id: uuidv4(), variable: "", type: ConditionType.STR },
    ]);
    const [outputs, setOutputs] = useState<NewRuleOutput[]>([
        { id: uuidv4(), variable: "", type: ConditionType.STR },
    ]);
    const rulenameRef = useRef<HTMLInputElement>(null);
    const ruletypeRef = useRef<HTMLSelectElement>(null);
    const rulestrategyRef = useRef<HTMLSelectElement>(null);
    // handling Conditions
    const handleAddCondition = () => {
        const condition: NewRuleCondition = {
            id: uuidv4(),
            variable: "",
            type: ConditionType.STR,
        };
        const newasdf = [...conditions, { ...condition }];

        setConditions(newasdf);
    };
    const handleChangeCondition = (id: string, value: string) => {
        setConditions(
            conditions.map((x) => (x.id === id ? { ...x, variable: value } : x))
        );
    };
    const handleChangeConditionType = (id: string, value: string) => {
        setConditions(
            conditions.map((x) => (x.id === id ? { ...x, type: value } : x))
        );
    };
    const handleDelCondition = (id: string) => {
        setConditions(conditions.filter((x) => x.id !== id));
    };
    // handling Outputs
    const handleAddOutput = () => {
        const output: NewRuleOutput = {
            id: uuidv4(),
            variable: "",
            type: ConditionType.STR,
        };
        setOutputs([...outputs, { ...output }]);
    };
    const handleChangeOutput = (id: string, value: string) => {
        setOutputs(
            outputs.map((x) => (x.id === id ? { ...x, variable: value } : x))
        );
    };
    const handleChangeOutputType = (id: string, value: string) => {
        setOutputs(
            outputs.map((x) => (x.id === id ? { ...x, type: value } : x))
        );
    };
    const handleDelOutput = (id: string) => {
        setOutputs(outputs.filter((x) => x.id !== id));
    };
    // handle sending close
    const handleClose = () => {
        setShowSending(false);
    };
    // submit
    const handleSubmit = (event: FormEvent) => {
        event.preventDefault();
        setShowSending(true);

        const conds = conditions.map((x) => {
            const c: ParametersDto = {
                key: x.variable,
                typeof: x.type,
                usefor: "CONDITION",
            };
            return c;
        });

        const outs = outputs.map((x) => {
            const c: ParametersDto = {
                key: x.variable,
                typeof: x.type,
                usefor: "OUTPUT",
            };
            return c;
        });

        const newRule: CreateRuleDto = {
            name: rulenameRef.current?.value!,
            rule_type: "MATRIX",
            strategy: "EARLY",
            parameters: [...conds, ...outs],
        };

        const tenant = Vars.tenant;
        const tenantDto = JSON.parse(tenant) as TenantDto;

        axios
            .post<CreateRuleDto>(CREA_RULE(tenantDto.id.toString()), newRule, {
                headers: {
                    "Accept-Language": Vars.language,
                },
            })
            .then((res) => {
                console.log(res);
                switch (res.status) {
                    case 201:
                        setShowSending(false);
                        break;
                    default:
                        break;
                }
            })
            .catch((err: AxiosError) => {
                if (err.response) {
                    const data = err.response!.data as ErrorDto[];
                    setIsError(data);
                }
            });
    };

    return (
        <>
            {showSending && (
                <Loading02
                    title="Sending"
                    isFailure={isError.length > 0}
                    errorList={isError}
                    onClose={handleClose}
                ></Loading02>
            )}
            <Toolbar
                title={Messages.CREA_RULE}
                titleInfo={
                    <div>
                        <p>
                            Cree una regla indicando nombre, tipo y estrategia.
                        </p>
                        <p>
                            Defina los parámetros que serviran como condiciones
                            y salidas.
                        </p>
                    </div>
                }
                hideSearch
                onAction01={() => window.location.reload()}
                action01Icon="bi-recycle"
            ></Toolbar>
            <Container className="mt-3">
                <Form onSubmit={handleSubmit}>
                    <Row>
                        <Col>
                            <Form.Group className="mb-3" controlId="rulename">
                                <Form.Label>{Messages.RULENAME}</Form.Label>
                                <Form.Control
                                    placeholder="ru.domain.detail"
                                    required={true}
                                    minLength={5}
                                    maxLength={50}
                                    ref={rulenameRef}
                                />
                            </Form.Group>
                        </Col>
                        <Col>
                            <Form.Group className="mb-3" controlId="ruletype">
                                <Form.Label>{Messages.RULETYPE}</Form.Label>
                                <Form.Select required={true} ref={ruletypeRef}>
                                    <option>{Messages.RULETYPE_SELECT}</option>
                                    <option value={1}>{Messages.MATRIX}</option>
                                </Form.Select>
                            </Form.Group>
                        </Col>
                        <Col>
                            <Form.Group
                                className="mb-3"
                                controlId="rulestrategy"
                            >
                                <Form.Label>{Messages.RULESTRATEGY}</Form.Label>
                                <Form.Select
                                    required={true}
                                    ref={rulestrategyRef}
                                >
                                    <option>
                                        {Messages.RULESTRATEGY_SELECT}
                                    </option>
                                    <option value={1}>
                                        {Messages.RULESTRATEGY_EARLY}
                                    </option>
                                    <option value={2}>
                                        {Messages.RULESTRATEGY_BASE}
                                    </option>
                                    <option value={3}>
                                        {Messages.RULESTRATEGY_ALL}
                                    </option>
                                </Form.Select>
                            </Form.Group>
                        </Col>
                    </Row>

                    <Row>
                        <Col>
                            <Button onClick={handleAddCondition} size="sm">
                                <i className="bi bi-plus-lg"></i>
                                {" " + Messages.BUTTON_CONDITION}
                            </Button>
                            <Table striped bordered hover>
                                <thead>
                                    <tr>
                                        <th style={{ width: "0rem" }}></th>
                                        <th>{Messages.CONDNAME}</th>
                                        <th>{Messages.TYPE}</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {conditions.map((x, idx) => (
                                        <tr key={x.id}>
                                            <td>
                                                <Button
                                                    disabled={
                                                        idx == 0 &&
                                                        conditions.length == 1
                                                    }
                                                    onClick={() =>
                                                        handleDelCondition(x.id)
                                                    }
                                                    size="sm"
                                                    variant="danger"
                                                >
                                                    <i className="bi bi-x-lg"></i>
                                                </Button>
                                            </td>
                                            <td>
                                                <InputGroup className="mb-1">
                                                    <Form.Control
                                                        name={"cond-" + x.id}
                                                        onChange={(e) =>
                                                            handleChangeCondition(
                                                                x.id,
                                                                e.target.value
                                                            )
                                                        }
                                                        value={x.variable}
                                                        placeholder="conditionName"
                                                    />
                                                </InputGroup>
                                            </td>
                                            <td>
                                                <Form.Select
                                                    name={"condsel-" + x.id}
                                                    onChange={(e) =>
                                                        handleChangeConditionType(
                                                            x.id,
                                                            e.target.value
                                                        )
                                                    }
                                                    value={x.type}
                                                    aria-label="Default select example"
                                                >
                                                    <option>
                                                        {ConditionType.STR}
                                                    </option>
                                                    <option>
                                                        {ConditionType.NUM}
                                                    </option>
                                                    <option>
                                                        {ConditionType.BOOL}
                                                    </option>
                                                    <option>
                                                        {ConditionType.DATE}
                                                    </option>
                                                </Form.Select>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </Table>
                        </Col>
                        <Col>
                            <Button onClick={handleAddOutput} size="sm">
                                <i className="bi bi-plus-lg"></i>
                                {" " + Messages.BUTTON_OUTPUT}
                            </Button>
                            <Table striped bordered hover>
                                <thead>
                                    <tr>
                                        <th style={{ width: "0rem" }}></th>
                                        <th>{Messages.OUTNAME}</th>
                                        <th>{Messages.TYPE}</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {outputs.map((x) => (
                                        <tr key={x.id}>
                                            <td>
                                                <Button
                                                    onClick={() =>
                                                        handleDelOutput(x.id)
                                                    }
                                                    size="sm"
                                                    variant="danger"
                                                >
                                                    <i className="bi bi-x-lg"></i>
                                                </Button>
                                            </td>
                                            <td>
                                                <InputGroup className="mb-1">
                                                    <Form.Control
                                                        name={"out-" + x.id}
                                                        onChange={(e) =>
                                                            handleChangeOutput(
                                                                x.id,
                                                                e.target.value
                                                            )
                                                        }
                                                        value={x.variable}
                                                        placeholder="outputName"
                                                    />
                                                </InputGroup>
                                            </td>
                                            <td>
                                                <Form.Select
                                                    name={"outsel-" + x.id}
                                                    onChange={(e) =>
                                                        handleChangeOutputType(
                                                            x.id,
                                                            e.target.value
                                                        )
                                                    }
                                                    value={x.type}
                                                    aria-label="Default select example"
                                                >
                                                    <option>
                                                        {ConditionType.STR}
                                                    </option>
                                                    <option>
                                                        {ConditionType.NUM}
                                                    </option>
                                                    <option>
                                                        {ConditionType.BOOL}
                                                    </option>
                                                    <option>
                                                        {ConditionType.DATE}
                                                    </option>
                                                </Form.Select>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </Table>
                        </Col>
                    </Row>
                    <br></br>
                    <Row>
                        <Col className="text-end">
                            <Button variant="primary" type="submit">
                                {Messages.BUTTON_NEXT}
                            </Button>
                        </Col>
                    </Row>
                </Form>
            </Container>
        </>
    );
}

export default CreateRule;

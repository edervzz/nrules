import {
    Button,
    Col,
    Container,
    Form,
    InputGroup,
    OverlayTrigger,
    Row,
    Table,
    Tooltip,
} from "react-bootstrap";
import Messages from "../../locales/Messages";
import {
    NewRuleCondition,
    NewRuleOutput,
    CreateRuleDto,
    ParametersDto,
    ErrorDto,
} from "../../typings";
import { ConditionType } from "../../enums";
import { FormEvent, useRef, useState } from "react";
import Toolbar from "../../components/Toolbar";
import { v4 as uuidv4 } from "uuid";
import { Loading02 } from "../../components/Loading";
import { useNavigate } from "react-router-dom";
import {
    HandleAddCondition,
    handleAddOutput,
    handleChangeCondition,
    handleChangeConditionType,
    handleChangeOutput,
    handleChangeOutputType,
    handleClose,
    handleDelCondition,
    handleDelOutput,
} from "./Handlers";
import { PostRule } from "../../adapters/RuleAdapter";

interface Props {}

export default function CreateRule({}: Props) {
    const navigate = useNavigate();
    const [showSending, setShowSending] = useState(false);
    const [errorList, setErrorList] = useState<ErrorDto[]>([]);
    const [conditions, setConditions] = useState<NewRuleCondition[]>([
        { id: uuidv4(), variable: "", type: ConditionType.STR },
    ]);
    const [outputs, setOutputs] = useState<NewRuleOutput[]>([
        { id: uuidv4(), variable: "", type: ConditionType.STR },
    ]);
    const rulenameRef = useRef<HTMLInputElement>(null);
    const ruletypeRef = useRef<HTMLSelectElement>(null);
    const rulestrategyRef = useRef<HTMLSelectElement>(null);

    // submit
    const handleSubmit = (event: FormEvent) => {
        event.preventDefault();
        setShowSending(true);
        setErrorList([]);

        const conds = conditions.map((x) => {
            return {
                key: x.variable,
                typeof: x.type,
                usefor: "CONDITION",
            } as ParametersDto;
        });

        const outs = outputs.map((x) => {
            return {
                key: x.variable,
                typeof: x.type,
                usefor: "OUTPUT",
            } as ParametersDto;
        });

        const newRule: CreateRuleDto = {
            name: rulenameRef.current?.value!,
            rule_type: ruletypeRef.current?.value! == "1" ? "MATRIX" : "TREE",
            strategy: getStrategy(rulestrategyRef.current?.value!),
            parameters: [...conds, ...outs],
        };

        PostRule(newRule).then((result) => {
            if (result.ok) {
                setShowSending(false);
                const item = result.item!;
                const elements = item.split("/");
                const uuidobj = elements[elements.length - 1];
                navigate(`/editor/${uuidobj}`);
            } else {
                const data = result.errorList!;
                setErrorList(data);
            }
        });
    };

    const btnAddOutput = (
        <Button
            onClick={() => {
                window.location.reload();
            }}
            size="sm"
            variant="primary"
            type="submit"
        >
            <i className="bi bi-trash-fill"></i>
        </Button>
    );

    return (
        <>
            {showSending && (
                <Loading02
                    title={Messages.COMMON_SENDING}
                    isFailure={errorList.length > 0}
                    errorList={errorList}
                    onClose={() => handleClose(setShowSending)}
                ></Loading02>
            )}

            <Toolbar
                title={Messages.NEWRULE_CREA_RULE}
                titleInfo={
                    <div>
                        <p>{Messages.NEWRULE_INFO_01}</p>
                        <p>{Messages.NEWRULE_INFO_02}</p>
                    </div>
                }
                extraItems={[btnAddOutput]}
            ></Toolbar>

            <Container className="mt-3">
                <Form onSubmit={handleSubmit}>
                    <Row>
                        <Col>
                            <Form.Group className="mb-3" controlId="rulename">
                                <Form.Label>
                                    {Messages.NEWRULE_RULENAME}
                                </Form.Label>
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
                                <Form.Label>
                                    {Messages.NEWRULE_RULETYPE}
                                </Form.Label>
                                <Form.Select required={true} ref={ruletypeRef}>
                                    <option>
                                        {Messages.NEWRULE_RULETYPE_SELECT}
                                    </option>
                                    <option value={1}>
                                        {Messages.COMMON_MATRIX}
                                    </option>
                                </Form.Select>
                            </Form.Group>
                        </Col>
                        <Col>
                            <Form.Group
                                className="mb-3"
                                controlId="rulestrategy"
                            >
                                <Form.Label>
                                    {Messages.NEWRULE_RULESTRATEGY}
                                </Form.Label>
                                <Form.Select
                                    required={true}
                                    ref={rulestrategyRef}
                                >
                                    <option>
                                        {Messages.NEWRULE_RULESTRATEGY_SELECT}
                                    </option>
                                    <option value={1}>
                                        {Messages.NEWRULE_RULESTRATEGY_EARLY}
                                    </option>
                                    <option value={2}>
                                        {Messages.NEWRULE_RULESTRATEGY_BASE}
                                    </option>
                                    <option value={3}>
                                        {Messages.NEWRULE_RULESTRATEGY_ALL}
                                    </option>
                                </Form.Select>
                            </Form.Group>
                        </Col>
                    </Row>

                    <Row>
                        <Col>
                            <Button
                                onClick={() =>
                                    HandleAddCondition(
                                        conditions,
                                        setConditions
                                    )
                                }
                                size="sm"
                            >
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
                                                        handleDelCondition(
                                                            conditions,
                                                            setConditions,
                                                            x.id
                                                        )
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
                                                                conditions,
                                                                setConditions,
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
                                                            conditions,
                                                            setConditions,
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
                            <Button
                                onClick={() =>
                                    handleAddOutput(outputs, setOutputs)
                                }
                                size="sm"
                            >
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
                                                        handleDelOutput(
                                                            outputs,
                                                            setOutputs,
                                                            x.id
                                                        )
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
                                                                outputs,
                                                                setOutputs,
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
                                                            outputs,
                                                            setOutputs,
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

const getStrategy = (strategyCode: string) => {
    switch (strategyCode) {
        case "1":
            return "EARLY";
        case "2":
            return "BASE";
        default:
            return "ALL";
    }
};

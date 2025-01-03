import {
    Accordion,
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
    ErrorDto,
    NewRuleTag,
} from "../../models";
import { ConditionType } from "../../enums";
import { FormEvent, useRef, useState } from "react";
import Toolbar from "../../components/Toolbar";
import { v4 as uuidv4 } from "uuid";
import { LoadingErrorListModal } from "../../components/Loading";
import { useNavigate } from "react-router-dom";
import Storage from "../../storage";
import { TagDto } from "../../models/TagDto";

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

    const [tags, setTags] = useState<NewRuleTag[]>([]);

    const rulenameRef = useRef<HTMLInputElement>(null);
    const ruletypeRef = useRef<HTMLSelectElement>(null);
    const rulestrategyRef = useRef<HTMLSelectElement>(null);

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

        const tgs = tags.map((x) => {
            return {
                key: x.key,
                value: x.value,
            } as TagDto;
        });

        const newRule: CreateRuleDto = {
            name: rulenameRef.current?.value!,
            rule_type: ruletypeRef.current?.value! == "1" ? "MATRIX" : "TREE",
            strategy: getStrategy(rulestrategyRef.current?.value!),
            parameters: [...conds, ...outs],
            tags: [...tgs],
        };

        Storage.Rule.PostRule(newRule).then((result) => {
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

    const btnReload = (
        <Button
            onClick={() => {
                window.location.reload();
            }}
            size="sm"
            variant="primary"
            type="submit"
        >
            <i className="bi bi-eraser-fill"></i>
        </Button>
    );

    return (
        <>
            <LoadingErrorListModal
                show={showSending}
                title={Messages.COMMON_SENDING}
                isFailure={errorList.length > 0}
                errorList={errorList}
                onClose={() => setShowSending(false)}
            ></LoadingErrorListModal>

            <Toolbar
            // title={Messages.NEWRULE_CREA_RULE}
            // titleInfo={
            //     <div>
            //         <p>{Messages.NEWRULE_INFO_01}</p>
            //         <p>{Messages.NEWRULE_INFO_02}</p>
            //     </div>
            // }
            // extraItems={[btnReload]}
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
                            <Table striped bordered hover>
                                <thead>
                                    <tr>
                                        <th style={{ width: "0rem" }}>
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
                                            </Button>
                                        </th>
                                        <th>{Messages.CONDITIONS}</th>
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
                                                        placeholder={
                                                            Messages.CONDITIONNAME
                                                        }
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
                            <Table striped bordered hover>
                                <thead>
                                    <tr>
                                        <th style={{ width: "0rem" }}>
                                            <Button
                                                onClick={() =>
                                                    handleAddOutput(
                                                        outputs,
                                                        setOutputs
                                                    )
                                                }
                                                size="sm"
                                            >
                                                <i className="bi bi-plus-lg"></i>
                                            </Button>
                                        </th>
                                        <th>{Messages.OUTPUTS}</th>
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

                    <Row>
                        <Accordion defaultActiveKey="0">
                            <Accordion.Item eventKey="0">
                                <Accordion.Header>
                                    {Messages.TAGS}
                                </Accordion.Header>
                                <Accordion.Body>
                                    <Table striped bordered hover>
                                        <thead>
                                            <tr>
                                                <th style={{ width: "0rem" }}>
                                                    <Button
                                                        onClick={() =>
                                                            handleAddTag(
                                                                tags,
                                                                setTags
                                                            )
                                                        }
                                                        size="sm"
                                                    >
                                                        <i className="bi bi-plus-lg"></i>
                                                    </Button>
                                                </th>
                                                <th>{Messages.KEY}</th>
                                                <th>{Messages.VALUE}</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {tags.map((x) => (
                                                <tr key={x.id}>
                                                    <td>
                                                        <Button
                                                            onClick={() =>
                                                                handleDelTag(
                                                                    tags,
                                                                    setTags,
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
                                                                name={
                                                                    "key-" +
                                                                    x.id
                                                                }
                                                                onChange={(e) =>
                                                                    handleChangeTagKey(
                                                                        tags,
                                                                        setTags,
                                                                        x.id,
                                                                        e.target
                                                                            .value
                                                                    )
                                                                }
                                                                value={x.key}
                                                                placeholder="key"
                                                            />
                                                        </InputGroup>
                                                    </td>
                                                    <td>
                                                        <InputGroup className="mb-1">
                                                            <Form.Control
                                                                name={
                                                                    "val-" +
                                                                    x.id
                                                                }
                                                                onChange={(e) =>
                                                                    handleChangeTagValue(
                                                                        tags,
                                                                        setTags,
                                                                        x.id,
                                                                        e.target
                                                                            .value
                                                                    )
                                                                }
                                                                value={x.value}
                                                                placeholder="value"
                                                            />
                                                        </InputGroup>
                                                    </td>
                                                </tr>
                                            ))}
                                        </tbody>
                                    </Table>
                                </Accordion.Body>
                            </Accordion.Item>
                        </Accordion>
                    </Row>
                    <br></br>
                    <Row>
                        <Col className="text-end">
                            <Button
                                onClick={() => {
                                    window.location.reload();
                                }}
                                variant="secondary"
                                className="me-2"
                            >
                                <i className="bi bi-eraser"></i>
                            </Button>

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

/* Handlers
 */
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

const HandleAddCondition = (
    conditions: NewRuleCondition[],
    setConditions: React.Dispatch<React.SetStateAction<NewRuleCondition[]>>
) => {
    const condition: NewRuleCondition = {
        id: uuidv4(),
        variable: "",
        type: ConditionType.STR,
    };
    const newConditions = [...conditions, { ...condition }];
    setConditions(newConditions);
};

const handleChangeCondition = (
    conditions: NewRuleCondition[],
    setConditions: React.Dispatch<React.SetStateAction<NewRuleCondition[]>>,
    id: string,
    value: string
) => {
    setConditions(
        conditions.map((x) => (x.id === id ? { ...x, variable: value } : x))
    );
};

const handleChangeConditionType = (
    conditions: NewRuleCondition[],
    setConditions: React.Dispatch<React.SetStateAction<NewRuleCondition[]>>,
    id: string,
    value: string
) => {
    setConditions(
        conditions.map((x) => (x.id === id ? { ...x, type: value } : x))
    );
};

const handleDelCondition = (
    conditions: NewRuleCondition[],
    setConditions: React.Dispatch<React.SetStateAction<NewRuleCondition[]>>,
    id: string
) => {
    setConditions(conditions.filter((x) => x.id !== id));
};

const handleAddOutput = (
    outputs: NewRuleOutput[],
    setOutputs: React.Dispatch<React.SetStateAction<NewRuleOutput[]>>
) => {
    const output: NewRuleOutput = {
        id: uuidv4(),
        variable: "",
        type: ConditionType.STR,
    };
    setOutputs([...outputs, { ...output }]);
};

const handleChangeOutput = (
    outputs: NewRuleOutput[],
    setOutputs: React.Dispatch<React.SetStateAction<NewRuleOutput[]>>,
    id: string,
    value: string
) => {
    setOutputs(
        outputs.map((x) => (x.id === id ? { ...x, variable: value } : x))
    );
};

const handleChangeOutputType = (
    outputs: NewRuleOutput[],
    setOutputs: React.Dispatch<React.SetStateAction<NewRuleOutput[]>>,
    id: string,
    value: string
) => {
    setOutputs(outputs.map((x) => (x.id === id ? { ...x, type: value } : x)));
};

const handleDelOutput = (
    outputs: NewRuleOutput[],
    setOutputs: React.Dispatch<React.SetStateAction<NewRuleOutput[]>>,
    id: string
) => {
    setOutputs(outputs.filter((x) => x.id !== id));
};

const handleAddTag = (
    tags: NewRuleTag[],
    setOutputs: React.Dispatch<React.SetStateAction<NewRuleTag[]>>
) => {
    const tag: NewRuleTag = {
        id: uuidv4(),
        key: "",
        value: "",
    };
    setOutputs([...tags, { ...tag }]);
};

const handleChangeTagKey = (
    outputs: NewRuleTag[],
    setOutputs: React.Dispatch<React.SetStateAction<NewRuleTag[]>>,
    id: string,
    value: string
) => {
    setOutputs(outputs.map((x) => (x.id === id ? { ...x, key: value } : x)));
};

const handleChangeTagValue = (
    outputs: NewRuleTag[],
    setOutputs: React.Dispatch<React.SetStateAction<NewRuleTag[]>>,
    id: string,
    value: string
) => {
    setOutputs(outputs.map((x) => (x.id === id ? { ...x, value: value } : x)));
};

const handleDelTag = (
    tags: NewRuleTag[],
    setTags: React.Dispatch<React.SetStateAction<NewRuleTag[]>>,
    id: string
) => {
    setTags(tags.filter((x) => x.id !== id));
};

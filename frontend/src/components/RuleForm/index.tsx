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
import { NewRuleCondition, NewRuleOutput, NewRuleTag } from "../../models";
import { ConditionType } from "../../enums";
import { FormEvent, useRef, useState } from "react";
import { v4 as uuidv4 } from "uuid";

interface Props {
    onSubmit: (
        rulename: string,
        ruletype: string,
        strategy: string,
        conditions: NewRuleCondition[],
        outputs: NewRuleOutput[],
        tags: NewRuleTag[]
    ) => void;
}

export default function RuleForm({ onSubmit }: Props) {
    // 1. States
    const [conditions, setConditions] = useState<NewRuleCondition[]>([
        { id: uuidv4(), variable: "", type: ConditionType.STR },
    ]);
    const [outputs, setOutputs] = useState<NewRuleOutput[]>([
        { id: uuidv4(), variable: "", type: ConditionType.STR },
    ]);
    const [tags, setTags] = useState<NewRuleTag[]>([]);

    // 2. Ref
    const nameRef = useRef<HTMLInputElement>(null);
    const typeRef = useRef<HTMLSelectElement>(null);
    const strategyRef = useRef<HTMLSelectElement>(null);
    // 3. Handlers
    const handleSubmit = (event: FormEvent) => {
        event.preventDefault();
        onSubmit(
            nameRef.current?.value || "",
            typeRef.current?.value || "",
            getStrategy(strategyRef.current?.value || ""),
            conditions,
            outputs,
            tags
        );
    };

    return (
        <Container className="mt-3">
            <Form onSubmit={handleSubmit}>
                <Row>
                    <Col>
                        <Form.Group className="mb-3" controlId="rulename">
                            <Form.Label>{Messages.NEWRULE_RULENAME}</Form.Label>
                            <Form.Control
                                placeholder="ru.domain.detail"
                                required={true}
                                minLength={5}
                                maxLength={50}
                                ref={nameRef}
                            />
                        </Form.Group>
                    </Col>
                    <Col>
                        <Form.Group className="mb-3" controlId="ruletype">
                            <Form.Label>{Messages.NEWRULE_RULETYPE}</Form.Label>
                            <Form.Select required={true} ref={typeRef}>
                                <option value={0}>
                                    {Messages.NEWRULE_RULETYPE_SELECT}
                                </option>
                                <option value={1}>
                                    {Messages.COMMON_TABLE}
                                </option>
                                <option value={2}>
                                    {Messages.COMMON_TREE}
                                </option>
                            </Form.Select>
                        </Form.Group>
                    </Col>
                    <Col>
                        <Form.Group className="mb-3" controlId="rulestrategy">
                            <Form.Label>
                                {Messages.NEWRULE_RULESTRATEGY}
                            </Form.Label>
                            <Form.Select required={true} ref={strategyRef}>
                                <option value={1}>
                                    {Messages.NEWRULE_RULESTRATEGY_EARLY}
                                </option>
                            </Form.Select>
                        </Form.Group>
                    </Col>
                </Row>

                {/* <Row>
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
                </Row> */}

                <Row>
                    <Accordion defaultActiveKey="0">
                        <Accordion.Item eventKey="0">
                            <Accordion.Header>{Messages.TAGS}</Accordion.Header>
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
                                                            name={"key-" + x.id}
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
                                                            name={"val-" + x.id}
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

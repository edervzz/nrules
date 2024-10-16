import { Button, Form, InputGroup, Table } from "react-bootstrap";
import { NewRuleOutput } from "../../../typings";
import { ConditionType } from "../../../enums";
import Messages from "../../../locales/Messages";

interface Props {
    outputs: NewRuleOutput[];
    onDeleteOutput: (id: number) => void;
    onChangeOutput: (id: number, value: string) => void;
    onChangeOutputType: (id: number, value: string) => void;
    onAddOutput: () => void;
}

function Step03({
    outputs,
    onDeleteOutput,
    onChangeOutput,
    onChangeOutputType,
    onAddOutput,
}: Props) {
    return (
        <>
            <br />
            <Button onClick={onAddOutput} size="sm">
                <i className="bi bi-plus-lg"></i>
                {" " + Messages.BUTTON_OUTPUT}
            </Button>

            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th style={{ width: "0rem" }}></th>
                        <th>{Messages.NAME}</th>
                        <th>{Messages.TYPE}</th>
                    </tr>
                </thead>
                <tbody>
                    {outputs.map((x, idx) => (
                        <tr key={x.id}>
                            <td>
                                {idx !== 0 && (
                                    <Button
                                        onClick={() => onDeleteOutput(x.id)}
                                        size="sm"
                                        variant="danger"
                                    >
                                        <i className="bi bi-x-lg"></i>
                                    </Button>
                                )}
                            </td>
                            <td>
                                <InputGroup className="mb-1">
                                    <Form.Control
                                        onChange={(e) =>
                                            onChangeOutput(x.id, e.target.value)
                                        }
                                        value={x.variable}
                                        placeholder="fieldName"
                                    />
                                </InputGroup>
                            </td>
                            <td>
                                <Form.Select
                                    onChange={(e) =>
                                        onChangeOutputType(x.id, e.target.value)
                                    }
                                    value={x.type}
                                    aria-label="Default select example"
                                >
                                    <option>{ConditionType.STR}</option>
                                    <option>{ConditionType.NUM}</option>
                                    <option>{ConditionType.BOOL}</option>
                                    <option>{ConditionType.DATE}</option>
                                </Form.Select>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </>
    );
}

export default Step03;

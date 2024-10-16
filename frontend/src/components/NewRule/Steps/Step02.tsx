import { Button, Form, InputGroup, Table } from "react-bootstrap";
import { NewRuleCondition } from "../../../typings";
import { ConditionType } from "../../../enums";
import Messages from "../../../locales/Messages";

interface Props {
    conditions: NewRuleCondition[];
    onDeleteCondition: (id: number) => void;
    onChangeCondition: (id: number, value: string) => void;
    onChangeConditionType: (id: number, value: string) => void;
    onAddCondition: () => void;
}

function Step02({
    conditions,
    onDeleteCondition,
    onChangeCondition,
    onChangeConditionType,
    onAddCondition,
}: Props) {
    return (
        <>
            <br />
            <Button onClick={onAddCondition} size="sm">
                <i className="bi bi-plus-lg"></i>
                {" " + Messages.BUTTON_CONDITION}
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
                    {conditions.map((x, idx) => (
                        <tr key={x.id}>
                            <td>
                                {idx !== 0 && (
                                    <Button
                                        onClick={() => onDeleteCondition(x.id)}
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
                                            onChangeCondition(
                                                x.id,
                                                e.target.value
                                            )
                                        }
                                        value={x.variable}
                                        placeholder="fieldName"
                                    />
                                </InputGroup>
                            </td>
                            <td>
                                <Form.Select
                                    onChange={(e) =>
                                        onChangeConditionType(
                                            x.id,
                                            e.target.value
                                        )
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

export default Step02;

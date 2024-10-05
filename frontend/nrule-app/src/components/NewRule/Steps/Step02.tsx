import { Button, Form, InputGroup, Table } from "react-bootstrap";
import { NewRuleCondition } from "../../../typings";
import { ConditionType } from "../../../enums/operator";
import Messages from "../../../locales/Messages";

type Props = {
    conditions: NewRuleCondition[];
    onDelete: (id: number) => void;
    onChangeVariable: (id: number, value: string) => void;
    onChangeType: (id: number, value: string) => void;
    onAdd: () => void;
};

function Step02({
    conditions,
    onDelete,
    onChangeVariable,
    onChangeType,
    onAdd,
}: Props) {
    return (
        <>
            <Button onClick={onAdd} size="sm">
                <i className="bi bi-plus-lg"></i>
                {" " + Messages.BUTTON_ADD}
            </Button>

            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th style={{ width: "0rem" }}></th>
                        <th>Name</th>
                        <th>Type</th>
                    </tr>
                </thead>
                <tbody>
                    {conditions.map((x, idx) => (
                        <tr key={x.id}>
                            <td>
                                {idx !== 0 && (
                                    <Button
                                        onClick={() => onDelete(x.id)}
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
                                            onChangeVariable(
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
                                        onChangeType(x.id, e.target.value)
                                    }
                                    value={x.type}
                                    aria-label="Default select example"
                                >
                                    <option>{ConditionType.STR}</option>
                                    <option>{ConditionType.NUM}</option>
                                    <option>{ConditionType.BOOL}</option>
                                    <option>{ConditionType.DATE}</option>
                                    <option>{ConditionType.TIME}</option>
                                    <option>{ConditionType.DTIME}</option>
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

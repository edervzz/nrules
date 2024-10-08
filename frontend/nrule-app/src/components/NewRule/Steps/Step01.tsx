import { Form } from "react-bootstrap";
import Messages from "../../../locales/Messages";

type Props = {
    rulename: string;
    ruletype: number;
    onRuleNameChange: (v: string) => void;
    onRuleTypeChange: (v: number) => void;
    isError: boolean;
};

function Step01({
    rulename,
    ruletype,
    onRuleNameChange,
    onRuleTypeChange,
    isError,
}: Props) {
    return (
        <Form>
            <Form.Group className="mb-3" controlId="rulename">
                <br />
                <Form.Label>{Messages.RULENAME}</Form.Label>
                <Form.Control
                    onChange={(e) => onRuleNameChange(e.target.value)}
                    value={rulename}
                    placeholder="ru.domain.detail"
                    required={true}
                    minLength={5}
                    maxLength={50}
                />
                {isError && (
                    <p className="text-danger">{Messages.CREA_RULE_001}</p>
                )}
            </Form.Group>
            <Form.Group className="mb-3" controlId="ruletype">
                <Form.Label>{Messages.RULETYPE}</Form.Label>
                <Form.Select
                    onChange={(e) => onRuleTypeChange(parseInt(e.target.value))}
                    value={ruletype}
                    aria-label="Default select example"
                >
                    <option value={0}>{Messages.RULETYPE_SELECT}</option>
                    <option value={1}>{Messages.TABLE}</option>
                    <option value={2}>{Messages.TREE}</option>
                </Form.Select>
            </Form.Group>
        </Form>
    );
}

export default Step01;

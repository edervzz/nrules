import { Form } from "react-bootstrap";
import Messages from "../../../locales/Messages";

type Props = {
    rulename: string;
    ruletype: number;
    rulestrategy: number;
    onRuleNameChange: (v: string) => void;
    onRuleTypeChange: (v: number) => void;
    onRuleStrategyChange: (v: number) => void;
    isError: boolean;
};

function Step01({
    rulename,
    ruletype,
    rulestrategy,
    onRuleNameChange,
    onRuleTypeChange,
    onRuleStrategyChange,
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
                >
                    <option value={0}>{Messages.RULETYPE_SELECT}</option>
                    <option value={1}>{Messages.TABLE}</option>
                </Form.Select>
            </Form.Group>
            <Form.Group className="mb-3" controlId="rulestrategy">
                <Form.Label>{Messages.RULESTRATEGY}</Form.Label>
                <Form.Select
                    onChange={(e) =>
                        onRuleStrategyChange(parseInt(e.target.value))
                    }
                    value={rulestrategy}
                >
                    <option value={0}>{Messages.RULESTRATEGY_SELECT}</option>
                    <option value={1}>{Messages.RULESTRATEGY_EARLY}</option>
                    <option value={2}>{Messages.RULESTRATEGY_BASE}</option>
                    <option value={3}>{Messages.RULESTRATEGY_ALL}</option>
                </Form.Select>
            </Form.Group>
        </Form>
    );
}

export default Step01;

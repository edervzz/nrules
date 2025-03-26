import { Button, Form, Stack } from "react-bootstrap";
import { useState } from "react";
import styles from "./Condition.module.css";
import Operator from "../Operator";

interface Props {
    variable: string;
    case_id: string;
    rule_id: string;
    op: string;
    value: string;
    isEdit: boolean;
    onChangeCondition: (op: string, val: string) => void;
}

export default function Condition({
    op,
    value,
    isEdit,
    onChangeCondition,
}: Props) {
    const [operator, setOperator] = useState(op);
    const [valueInternal, setValueInternal] = useState(value);
    const [showOperator, setShowOperator] = useState(false);
    const [textarea, setTextarea] = useState(false);

    return (
        <>
            {showOperator && (
                <Operator
                    onCancel={() => {
                        setShowOperator(false);
                    }}
                    onSelectOperator={(op) => {
                        onChangeCondition(op, value);
                        setOperator(op);
                        setShowOperator(false);
                    }}
                ></Operator>
            )}

            <Stack direction="horizontal" className={`${styles.myStack}`}>
                <Button
                    size="sm"
                    variant="outline-primary"
                    disabled={isEdit}
                    onClick={(_) => setShowOperator(!showOperator)}
                >
                    {operator}
                </Button>
                <Form.Control
                    disabled={isEdit}
                    value={valueInternal}
                    as={textarea ? "textarea" : "input"}
                    onDoubleClick={(e) => {
                        setTextarea(!textarea);
                    }}
                    onChange={(e) => {
                        setValueInternal(e.currentTarget.value);
                        onChangeCondition(operator, e.currentTarget.value);
                    }}
                />
            </Stack>
        </>
    );
}

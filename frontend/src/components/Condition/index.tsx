import { Button, Form, Stack } from "react-bootstrap";
import { useState } from "react";
import styles from "./Condition.module.css";

interface Props {
    op: string;
    value: string;
    onSelect: () => void;
}

export default function Condition({ op, value, onSelect }: Props) {
    const [operator, setOperator] = useState(op);

    return (
        <Stack direction="horizontal" className={`${styles.myStack}`}>
            <Button
                size="sm"
                variant="outline-primary"
                onClick={(_) => onSelect()}
            >
                {op}
            </Button>
            <Form.Control />
        </Stack>
    );
}

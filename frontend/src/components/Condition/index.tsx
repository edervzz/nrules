import { Button, Form, Stack } from "react-bootstrap";
import { useState } from "react";
import styles from "./Condition.module.css";

interface Props {
    op: string;
    value: string;
}

export default function Condition({ op, value }: Props) {
    const [operator, setOperator] = useState(op);

    return (
        <Stack direction="horizontal" className={`${styles.myStack}`}>
            <Button
                size="sm"
                variant="outline-primary"
                className={`${styles.myButton}`}
            >
                {op}
            </Button>
            <Form.Control value={value} />
        </Stack>
    );
}

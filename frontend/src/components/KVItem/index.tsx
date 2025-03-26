import { Form } from "react-bootstrap";
import { useState } from "react";
import styles from "./KVItem.module.css";

interface Props {
    value: string;
    isEdit: boolean;
    onChangeValue: (val: string) => void;
}

export default function KVItem({ value, isEdit, onChangeValue }: Props) {
    const [valueInternal, setValueInternal] = useState(value);

    return (
        <>
            <Form.Control
                disabled={isEdit}
                value={valueInternal}
                className={`${styles.myField}`}
                onChange={(e) => {
                    setValueInternal(e.currentTarget.value);
                    onChangeValue(e.currentTarget.value);
                }}
            />
        </>
    );
}

import { Button, Form, Stack, Table } from "react-bootstrap";
import { ParametersDto, CaseDto } from "../../models";
import { typeofparam } from "../../tools";
import { ConditionDto } from "../../models/ConditionDto";
import { KVItemDto } from "../../models/KVItemDto";
import { useState } from "react";
import Condition from "../Condition";
import KVItem from "../KVItem";
import styles from "./TableEditor.module.css";

interface Props {
    cases: CaseDto[];
    conditions: ConditionDto[];
    kvitems: KVItemDto[];
    inputs: ParametersDto[];
    outputs: ParametersDto[];
    isEdit?: boolean;
    onSelectedCase: (id: string) => void;
    onChangeCondition: (
        variable: string,
        case_id: string,
        rule_id: string,
        op: string,
        value: string
    ) => void;
    onChangeKVItem: (
        key: string,
        case_id: string,
        rule_id: string,
        value: string,
        calculation: string
    ) => void;
}

function TableEditor({
    cases,
    conditions,
    kvitems,
    inputs,
    outputs,
    isEdit = true,
    onSelectedCase,
    onChangeCondition,
    onChangeKVItem,
}: Props) {
    const [caseSelected, setCaseSelected] = useState("");

    const selectedCase = (id: string) => {
        setCaseSelected(id);
        onSelectedCase(id);
    };

    const deactiveColor = "#ba0012";
    const selectedcond = "#fbf3c5";
    const selectedkv = "#fbf3c5";

    return (
        <div className={`${styles.editor}`}>
            <Table bsPrefix="ctable" bordered hover>
                <thead className={"text-center " + `${styles.header}`}>
                    <tr>
                        <th className={`${styles.corner_left}`}>#</th>

                        {inputs.map((x, idx) => (
                            <th key={x.key} className={`${styles.inputs}`}>
                                {x.key}
                                <br />
                                <div
                                    className={`${styles.typeparam}`}
                                    onDoubleClick={() => {}}
                                >
                                    {typeofparam(x.typeof)}
                                </div>
                            </th>
                        ))}
                        {outputs.map((x) => (
                            <th key={x.key} className={`${styles.outputs}`}>
                                {x.key}
                                <br />
                                {typeofparam(x.typeof)}
                            </th>
                        ))}
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {cases
                        .filter((x) => x.position > 0)
                        .map((c, idx) => (
                            <tr key={"case" + idx}>
                                <td
                                    key={"case-data" + idx}
                                    className={`${styles.caseNumber}`}
                                >
                                    {
                                        <Stack direction="horizontal">
                                            <Button
                                                variant="outline-success"
                                                size="sm"
                                                style={{
                                                    paddingLeft: ".3rem",
                                                    paddingRight: ".3rem",
                                                    marginRight: "10px",
                                                }}
                                            >
                                                <i className="bi bi-lightning-fill"></i>
                                            </Button>
                                            <Form.Check
                                                className="text-center mx-1"
                                                isValid={c.is_active}
                                                isInvalid={!c.is_active}
                                                reverse
                                                key={c.id}
                                                label={
                                                    c.position == 9999 ? (
                                                        <i className="bi bi-asterisk"></i>
                                                    ) : (
                                                        c.position
                                                    )
                                                }
                                                aria-label={"option " + c.id}
                                                checked={caseSelected == c.id}
                                                onChange={(_) => {}}
                                                onClick={(_) =>
                                                    c.id == caseSelected
                                                        ? selectedCase("")
                                                        : selectedCase(c.id)
                                                }
                                            />
                                        </Stack>
                                    }
                                </td>

                                {conditions
                                    .filter(
                                        (x) =>
                                            x.case_id == c.id &&
                                            x.rule_id == c.rule_id
                                    )
                                    .map((i) => (
                                        <td
                                            key={i.variable}
                                            className={`${styles.condition}`}
                                            style={{
                                                background:
                                                    c.id == caseSelected
                                                        ? selectedcond
                                                        : "",
                                                textDecoration: c.is_active
                                                    ? ""
                                                    : "line-through double",
                                            }}
                                        >
                                            <Condition
                                                variable={i.variable}
                                                case_id={i.case_id}
                                                rule_id={i.rule_id}
                                                op={i.operator}
                                                value={i.value}
                                                isEdit={isEdit}
                                                onChangeCondition={(op, val) =>
                                                    onChangeCondition(
                                                        i.variable,
                                                        i.case_id,
                                                        i.rule_id,
                                                        op,
                                                        val
                                                    )
                                                }
                                            ></Condition>
                                        </td>
                                    ))}
                                {kvitems
                                    .filter(
                                        (x) =>
                                            x.case_id == c.id &&
                                            x.rule_id == c.rule_id
                                    )
                                    .map((i) => (
                                        <td
                                            key={i.key}
                                            className={`${styles.kvitem}`}
                                            style={{
                                                color: c.is_active
                                                    ? ""
                                                    : deactiveColor,
                                                background:
                                                    c.id == caseSelected
                                                        ? selectedkv
                                                        : "",
                                                textDecoration: c.is_active
                                                    ? ""
                                                    : "line-through double",
                                            }}
                                        >
                                            <KVItem
                                                value={i.value}
                                                isEdit={isEdit}
                                                onChangeValue={(val) =>
                                                    onChangeKVItem(
                                                        i.key,
                                                        i.case_id,
                                                        i.rule_id,
                                                        val,
                                                        i.calculation
                                                    )
                                                }
                                            ></KVItem>
                                        </td>
                                    ))}
                            </tr>
                        ))}
                </tbody>
            </Table>
        </div>
    );
}

export default TableEditor;

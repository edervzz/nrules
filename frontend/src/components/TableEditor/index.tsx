import {
    Button,
    Container,
    Form,
    OverlayTrigger,
    Table,
    Tooltip,
} from "react-bootstrap";
import Messages from "../../locales/Messages";
import { ParametersDto, CaseDto } from "../../models";
import { DATE, JSON, NUMERIC, STRING, typeofparam } from "../../tools";
import { ConditionDto } from "../../models/ConditionDto";
import { KVItemDto } from "../../models/KVItemDto";
import { useState } from "react";
import Condition from "../Condition";

interface Props {
    cases: CaseDto[];
    conditions: ConditionDto[];
    kvitems: KVItemDto[];
    inputs: ParametersDto[];
    outputs: ParametersDto[];
    isUpdate: boolean;
    hideInactive?: boolean;
    onSelectedCase: (id: string) => void;
}

function TableEditor({
    cases,
    conditions,
    kvitems,
    inputs,
    outputs,
    isUpdate,
    hideInactive,
    onSelectedCase,
}: Props) {
    const [caseSelected, setCaseSelected] = useState("");

    const selectedCase = (id: string) => {
        setCaseSelected(id);
        onSelectedCase(id);
    };

    const deactiveColor = "#ba0012";

    return (
        <Table striped borderless size="sm" responsive="sm">
            <thead>
                <tr>
                    <th></th>
                    <th style={{ minWidth: "100px" }}>#</th>
                    {inputs.map((x) => (
                        <th
                            key={x.key}
                            className="fs-6 fw-medium"
                            style={{
                                borderLeft: "3px solid #6a329f",
                                backgroundColor: "#dfbcff",
                            }}
                        >
                            {x.key}
                            <br />
                            {typeofparam(x.typeof)}
                        </th>
                    ))}
                    {outputs.map((x) => (
                        <th
                            key={x.key}
                            className="fs-6 fw-medium"
                            style={{
                                borderLeft: "3px solid #00cc99",
                                backgroundColor: "#c8fff1",
                            }}
                        >
                            {x.key}
                            <br />
                            {typeofparam(x.typeof)}
                        </th>
                    ))}
                </tr>
            </thead>
            <tbody>
                {cases
                    .filter(
                        (x) =>
                            x.position > 0 &&
                            (x.is_active || !x.is_active == !hideInactive)
                    )
                    .map((c, idx) => (
                        <tr key={"case" + idx}>
                            <td key={"case-data" + idx}>
                                {
                                    <Form.Check
                                        isValid={c.is_active}
                                        isInvalid={!c.is_active}
                                        key={c.id}
                                        disabled={!isUpdate}
                                        aria-label={"option " + c.id}
                                        checked={caseSelected == c.id}
                                        onChange={(_) => {}}
                                        onClick={(_) =>
                                            c.id == caseSelected
                                                ? selectedCase("")
                                                : selectedCase(c.id)
                                        }
                                    />
                                }
                            </td>
                            <td
                                style={{
                                    color: c.is_active ? "" : deactiveColor,
                                    backgroundColor:
                                        c.position == 9999 ? "#fff2cc" : "",
                                    textDecoration: c.is_active
                                        ? ""
                                        : "line-through double",
                                }}
                            >
                                {c.position == 9999
                                    ? Messages.BYDEFAULT
                                    : c.position}
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
                                        style={{
                                            borderLeft: "3px solid #6a329f",
                                            backgroundColor:
                                                c.position == 9999
                                                    ? "#fff2cc"
                                                    : "",
                                            color: c.is_active
                                                ? ""
                                                : deactiveColor,
                                            textDecoration: c.is_active
                                                ? ""
                                                : "line-through double",
                                        }}
                                    >
                                        <Condition
                                            op={i.operator}
                                            value={i.value}
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
                                        style={{
                                            borderLeft: "3px solid #00cc99",
                                            backgroundColor:
                                                c.position == 9999
                                                    ? "#fff2cc"
                                                    : "",
                                            color: c.is_active
                                                ? ""
                                                : deactiveColor,
                                            textDecoration: c.is_active
                                                ? ""
                                                : "line-through double",
                                        }}
                                    >
                                        {i.value}
                                    </td>
                                ))}
                        </tr>
                    ))}
            </tbody>
        </Table>
    );
}

export default TableEditor;

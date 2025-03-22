import { Form, Table } from "react-bootstrap";
import { ParametersDto, CaseDto } from "../../models";
import { typeofparam } from "../../tools";
import { ConditionDto } from "../../models/ConditionDto";
import { KVItemDto } from "../../models/KVItemDto";
import { useState } from "react";
import Condition from "../Condition";
import KVItem from "../KVItem";

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
        <div
            style={{
                maxHeight: "calc(100vh - 80px)",
                overflowY: "scroll",
            }}
        >
            <Table bordered hover>
                <thead
                    className="text-center"
                    style={{ position: "sticky", top: "0", zIndex: 2 }}
                >
                    <tr>
                        <th
                            style={{
                                width: "50px",
                                position: "sticky",
                                top: "0",
                                left: "0",
                                zIndex: 2,
                            }}
                        >
                            #
                        </th>

                        {inputs.map((x, idx) => (
                            <th
                                key={x.key}
                                className="fs-6 fw-medium"
                                style={{
                                    width: "50px",
                                    borderLeft:
                                        idx > 0 ? "3px solid #7f73ff" : "",
                                    backgroundColor: "#e1c6fd",
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
                                    width: "50px",
                                    borderLeft: "3px solid #14d0f0",
                                    backgroundColor: "#b6e4fb",
                                }}
                            >
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
                                {/* selector */}
                                <td
                                    key={"case-data" + idx}
                                    style={{
                                        position: "sticky",
                                        left: 0,
                                        zIndex: 1,
                                    }}
                                >
                                    {
                                        <Form.Check
                                            className="text-center mx-2"
                                            isValid={c.is_active}
                                            isInvalid={!c.is_active}
                                            key={c.id}
                                            disabled={!isEdit}
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
                                    }
                                </td>

                                {conditions
                                    .filter(
                                        (x) =>
                                            x.case_id == c.id &&
                                            x.rule_id == c.rule_id
                                    )
                                    .map((i, index) => (
                                        <td
                                            key={i.variable}
                                            style={{
                                                borderLeft:
                                                    index > 0
                                                        ? "3px solid #7f73ff"
                                                        : "",
                                                backgroundColor:
                                                    c.position == 9999
                                                        ? "#fff2cc"
                                                        : "",
                                                color: c.is_active
                                                    ? ""
                                                    : deactiveColor,
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
                                            style={{
                                                borderLeft: "3px solid #14d0f0",
                                                backgroundColor:
                                                    c.position == 9999
                                                        ? "#fff2cc"
                                                        : "",
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

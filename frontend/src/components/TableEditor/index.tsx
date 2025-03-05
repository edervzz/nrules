import { Button, Container, Form, Table } from "react-bootstrap";
import Messages from "../../locales/Messages";
import { ParametersDto, CaseDto } from "../../models";
import { DATE, INPUT, JSON, NUMERIC, OUTPUT, STRING } from "../../tools";
import { ConditionDto } from "../../models/ConditionDto";
import { KVItemDto } from "../../models/KVItemDto";
import { useState } from "react";

interface Props {
    cases: CaseDto[];
    conditions: ConditionDto[];
    kvitems: KVItemDto[];
    inputs: ParametersDto[];
    outputs: ParametersDto[];
    isUpdate: boolean;
}

function TableEditor({
    cases,
    conditions,
    kvitems,
    inputs,
    outputs,
    isUpdate,
}: Props) {
    const [caseActive, setCaseActive] = useState("");
    return (
        <Container fluid>
            <Table striped bordered hover responsive size="md" style={{}}>
                <thead>
                    {/* <tr>
                        <th
                            style={{
                                minWidth: "200px",
                            }}
                            id="actions"
                            className="fs-6"
                        >
                            {Messages.CASES}
                        </th>
                        <th
                            style={{
                                borderLeft: "3px solid #b25afd",
                                minWidth: "200px",
                            }}
                            className="fs-6"
                            colSpan={inputs?.length || 0}
                            id={INPUT}
                        >
                            {Messages.CONDITIONS}
                        </th>
                        <th
                            style={{
                                borderLeft: "3px solid #49e048",
                                minWidth: "200px",
                            }}
                            className="fs-6"
                            colSpan={outputs?.length || 0}
                            id={OUTPUT}
                        >
                            {Messages.OUTPUTS}
                        </th>
                    </tr> */}
                    <tr>
                        <th></th>
                        {inputs.map((x) => (
                            <th
                                style={{
                                    borderLeft: "3px solid #b25afd",
                                    backgroundColor: "#e1ddfd",
                                }}
                                className="fs-6 fw-medium"
                                key={x.key}
                            >
                                {x.key}
                                {" - "}
                                {typeofparam(x.typeof)}
                            </th>
                        ))}
                        {outputs.map((x) => (
                            <th
                                style={{
                                    borderLeft: "3px solid #49e048",
                                    backgroundColor: "#baffb9",
                                }}
                                className="fs-6 fw-medium"
                                key={x.key}
                            >
                                {x.key}
                                {" - "}
                                {typeofparam(x.typeof)}
                            </th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {cases
                        .filter((x) => x.position > 0)
                        .map((c, idx) => (
                            <tr key={"case" + idx}>
                                <td key={"case-data" + idx}>
                                    <Form.Check
                                        isValid={c.is_active}
                                        isInvalid={!c.is_active}
                                        key={c.id.substring(0, 8)}
                                        disabled={!isUpdate}
                                        aria-label={
                                            "option " + c.id.substring(0, 8)
                                        }
                                        label={" " + c.position}
                                        checked={
                                            caseActive == c.id.substring(0, 8)
                                        }
                                        onClick={(e) =>
                                            c.id.substring(0, 8) == caseActive
                                                ? setCaseActive("")
                                                : setCaseActive(
                                                      c.id.substring(0, 8)
                                                  )
                                        }
                                    />
                                </td>
                                {conditions
                                    .filter(
                                        (x) =>
                                            x.case_id == c.id &&
                                            x.rule_id == c.rule_id
                                    )
                                    .map((i) => (
                                        <td key={i.variable}>
                                            {i.operator + " " + i.value}
                                        </td>
                                    ))}
                                {kvitems
                                    .filter(
                                        (x) =>
                                            x.case_id == c.id &&
                                            x.rule_id == c.rule_id
                                    )
                                    .map((i) => (
                                        <td key={i.key}>{i.value}</td>
                                    ))}
                            </tr>
                        ))}
                </tbody>
                <tfoot
                    style={{
                        borderTop: "3px solid #69686e",
                        backgroundColor: "#baffb9",
                    }}
                >
                    {cases
                        .filter((x) => x.position == 0)
                        .map((c, idx) => (
                            <tr key={"case" + idx}>
                                <td key={"case-data" + idx}>
                                    <Form.Check
                                        key={c.id.substring(0, 8)}
                                        disabled={!isUpdate}
                                        aria-label={
                                            "option " + c.id.substring(0, 8)
                                        }
                                        label={"Default"}
                                        checked={
                                            caseActive == c.id.substring(0, 8)
                                        }
                                        onClick={(e) =>
                                            c.id.substring(0, 8) == caseActive
                                                ? setCaseActive("")
                                                : setCaseActive(
                                                      c.id.substring(0, 8)
                                                  )
                                        }
                                    />
                                </td>
                                {conditions
                                    .filter(
                                        (x) =>
                                            x.case_id == c.id &&
                                            x.rule_id == c.rule_id
                                    )
                                    .map((i) => (
                                        <td key={i.variable}>
                                            {i.operator + " " + i.value}
                                        </td>
                                    ))}
                                {kvitems
                                    .filter(
                                        (x) =>
                                            x.case_id == c.id &&
                                            x.rule_id == c.rule_id
                                    )
                                    .map((i) => (
                                        <td key={i.key}>{i.value}</td>
                                    ))}
                            </tr>
                        ))}
                </tfoot>
            </Table>
        </Container>
    );
}

function typeofparam(t: string) {
    switch (t) {
        case STRING:
            return <i className="bi bi-alphabet-uppercase"></i>;
        case NUMERIC:
            return <i className="bi bi-123"></i>;
        case DATE:
            return <i className="bi bi-calendar-day"></i>;
        case JSON:
            return <i className="bi bi-filetype-json"></i>;
    }
}

export default TableEditor;

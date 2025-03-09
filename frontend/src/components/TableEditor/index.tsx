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
import { DATE, JSON, NUMERIC, STRING } from "../../tools";
import { ConditionDto } from "../../models/ConditionDto";
import { KVItemDto } from "../../models/KVItemDto";
import { useState } from "react";

interface Props {
    cases: CaseDto[];
    conditions: ConditionDto[];
    kvitems: KVItemDto[];
    inputs: ParametersDto[];
    outputs: ParametersDto[];
    fluid?: boolean | string | "sm" | "md" | "lg" | "xl" | "xxl";
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
    fluid = "xxl",
    isUpdate,
    hideInactive,
    onSelectedCase,
}: Props) {
    const [caseActive, setCaseActive] = useState("");

    const selectedCase = (id: string) => {
        setCaseActive(id);
        onSelectedCase(id);
    };

    const deactiveColor = "#ba0012";

    return (
        <Container fluid={fluid}>
            <Table striped hover responsive size="md" style={{}}>
                <thead>
                    <tr>
                        <th></th>
                        <th>#</th>
                        {inputs.map((x) => (
                            <th
                                style={{
                                    borderLeft: "3px solid #6a329f",
                                    backgroundColor: "#dfbcff",
                                }}
                                className="fs-6 fw-medium"
                                key={x.key}
                            >
                                {x.key}
                                <br />
                                {typeofparam(x.typeof)}
                            </th>
                        ))}
                        {outputs.map((x) => (
                            <th
                                style={{
                                    borderLeft: "3px solid #00cc99",
                                    backgroundColor: "#c8fff1",
                                }}
                                className="fs-6 fw-medium"
                                key={x.key}
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
                                    {c.position != 9999 && (
                                        <Form.Check
                                            isValid={c.is_active}
                                            isInvalid={!c.is_active}
                                            key={c.id}
                                            disabled={!isUpdate}
                                            aria-label={"option " + c.id}
                                            checked={caseActive == c.id}
                                            onChange={(_) => {}}
                                            onClick={(_) =>
                                                c.id == caseActive
                                                    ? selectedCase("")
                                                    : selectedCase(c.id)
                                            }
                                        />
                                    )}
                                </td>
                                <td
                                    style={{
                                        color: c.is_active ? "" : deactiveColor,
                                        textDecoration: c.is_active
                                            ? ""
                                            : "line-through double",
                                    }}
                                >
                                    {c.position == 9999
                                        ? Messages.BYDFAULT
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
                                                color: c.is_active
                                                    ? ""
                                                    : deactiveColor,
                                                textDecoration: c.is_active
                                                    ? ""
                                                    : "line-through double",
                                            }}
                                        >
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
                                        <td
                                            key={i.key}
                                            style={{
                                                borderLeft: "3px solid #00cc99",
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

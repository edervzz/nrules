import Session from "../../components/Session";
import Menubar from "../../components/Menubar";
import Messages from "../../locales/Messages";
import Editor from "./Editor";
import Toolbar from "../../components/Toolbar";
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { Rule } from "../../typings";
import Storage from "../../storage";
import { CaseDto, ParametersDto } from "../../models";
import { Button, ButtonGroup, Container, Form, Table } from "react-bootstrap";
import TableEditor from "../../components/TableEditor";
import { INPUT, OUTPUT } from "../../tools";
import { ConditionDto } from "../../models/ConditionDto";
import { KVItemDto } from "../../models/KVItemDto";

export default function EditorView() {
    // 1. States
    const { id } = useParams();
    const [edit, setEdit] = useState(false);
    const [cases, setCases] = useState<CaseDto[]>([]);
    const [conditions, setConditions] = useState<ConditionDto[]>([]);
    const [kvitems, setKVItems] = useState<KVItemDto[]>([]);
    const [inputs, setInputs] = useState<ParametersDto[]>([]);
    const [outputs, setOutputs] = useState<ParametersDto[]>([]);
    const [rule, setRule] = useState<Rule>({
        id: "",
        name: "",
        rule_type: "",
        strategy: "",
        version: 0,
        default_kvs: 0,
    });
    // 2. Handlers
    const handleUpdate = () => {
        setEdit(!edit);
    };
    // Effects
    useEffect(() => {
        Storage.Rule.GetRule(id || "").then((res) => {
            res.data && setRule(res.data);
            res.data &&
                setInputs(
                    res.data!.parameters?.filter((x) => x.usefor == INPUT) || []
                );
            res.data &&
                setOutputs(
                    res.data!.parameters?.filter((x) => x.usefor == OUTPUT) ||
                        []
                );
            res.data && setCases(res.data!.cases || []);
            res.data && setConditions(res.data!.conditions || []);
            res.data && setKVItems(res.data!.kvitems || []);
        });
    }, []);

    return (
        <Session>
            <Menubar
                fluid
                brand={Messages.NRULE}
                title={
                    (edit ? Messages.UPDATE : Messages.DISPLAY) +
                    ": " +
                    rule.name
                }
            ></Menubar>
            <Toolbar
                fluid
                title={rule.name}
                extraItems={[
                    <ButtonGroup aria-label="Basic example">
                        <Button
                            size="sm"
                            className="me-1"
                            variant={edit ? "success" : "outline-success"}
                            onClick={(_) => handleUpdate()}
                        >
                            <i className={"bi bi-pencil"} />
                        </Button>
                    </ButtonGroup>,
                    <ButtonGroup aria-label="Basic example">
                        <Button
                            // onClick={onAddRow}
                            name="adfas"
                            size="sm"
                            variant="primary"
                            className="me-1"
                            disabled={!edit}
                        >
                            <i className="bi bi-arrow-up"></i>
                        </Button>
                        <Button
                            // onClick={onAddRow}
                            name="adfas"
                            size="sm"
                            variant="primary"
                            className="me-1"
                            disabled={!edit}
                        >
                            <i className="bi bi-arrow-down"></i>
                        </Button>
                    </ButtonGroup>,

                    <ButtonGroup aria-label="Basic example">
                        <Button
                            // onClick={onAddRow}
                            name="adfas"
                            size="sm"
                            variant="primary"
                            className="me-1"
                            disabled={!edit}
                        >
                            <i className="bi bi-check-circle-fill"></i>
                        </Button>
                    </ButtonGroup>,

                    <ButtonGroup aria-label="Basic example">
                        <Button
                            // onClick={onAddRow}
                            name="adfas"
                            size="sm"
                            variant="primary"
                            className="me-1"
                            disabled={!edit}
                        >
                            <i className="bi bi-plus-lg"></i> {Messages.ROW}
                        </Button>

                        <Button
                            // onClick={() => setShowAdd("CONDITION")}
                            name="adfas"
                            size="sm"
                            variant="primary"
                            className="me-1"
                            disabled={!edit}
                        >
                            <i className="bi bi-plus-lg"></i>{" "}
                            {Messages.CONDITION}
                        </Button>

                        <Button
                            // onClick={() => setShowAdd("OUTPUT")}
                            name="adfas2"
                            size="sm"
                            variant="primary"
                            disabled={!edit}
                        >
                            <i className="bi bi-plus-lg"></i> {Messages.OUTPUT}
                        </Button>
                    </ButtonGroup>,

                    <ButtonGroup aria-label="Basic example">
                        <Button
                            // onClick={onAddRow}
                            name="adfas"
                            size="sm"
                            variant="primary"
                            className="me-1"
                            disabled={!edit}
                        >
                            {Messages.MENUBAR_TRANSPORTS}
                        </Button>
                    </ButtonGroup>,
                ]}
            />

            <TableEditor
                cases={cases}
                conditions={conditions}
                inputs={inputs}
                outputs={outputs}
                kvitems={kvitems}
                isUpdate={edit}
            />
        </Session>
    );
}

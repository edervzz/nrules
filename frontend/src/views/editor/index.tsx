import Session from "../../components/Session";
import Menubar from "../../components/Menubar";
import Messages from "../../locales/Messages";
import Toolbar from "../../components/Toolbar";
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { Rule } from "../../typings";
import Storage from "../../storage";
import {
    CaseDto,
    ParametersDto,
    NewCaseDto,
    NewParameterDto,
    NewParametersDto,
} from "../../models";
import { Button, ButtonGroup } from "react-bootstrap";
import TableEditor from "../../components/TableEditor";
import { INPUT, OUTPUT } from "../../tools";
import { ConditionDto } from "../../models/ConditionDto";
import { KVItemDto } from "../../models/KVItemDto";
import { ToastError, ToastWorking } from "../../components/Toasts";
import CaseForm from "../../components/CaseForm";
import Footer from "../../components/Footer/Footer";
import ConditionForm from "../../components/ConditionForm";
import KVItemForm from "../../components/KVItemForm";

export default function EditorView() {
    // 1. States
    const { id } = useParams();
    const [showToast, setShowToast] = useState(0);
    const [showCaseForm, setShowCaseForm] = useState(false);
    const [showConditionForm, setShowConditionForm] = useState(false);
    const [showKVItemForm, setShowKVItemForm] = useState(false);
    const [edit, setEdit] = useState(false);
    const [caseActive, setCaseActive] = useState("");
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

    const handleChangeCase = (
        caseIndex: number,
        caseIndex2: number,
        casesCopy: CaseDto[]
    ) => {
        setShowToast(1);
        let newCases = [...casesCopy];
        const aPos = newCases[caseIndex].position;
        const bPos = newCases[caseIndex2].position;
        newCases[caseIndex].position = bPos;
        newCases[caseIndex2].position = aPos;

        const data = {
            items: [newCases[caseIndex], newCases[caseIndex2]],
        };

        Storage.Case.PutCase(id || "", data)
            .then((res) => {
                if (res.ok) {
                    setShowToast(0);
                    newCases = newCases.sort((a, b) => a.position - b.position);
                    setCases(newCases);
                } else {
                    setShowToast(2);
                }
            })
            .catch((r) => {
                setShowToast(2);
            });
    };

    const handleActiveCase = (caseIndex: number, casesCopy: CaseDto[]) => {
        setShowToast(1);
        let newCases = [...casesCopy];
        newCases[caseIndex].is_active = !newCases[caseIndex].is_active;
        const data = {
            items: [newCases[caseIndex]],
        };

        Storage.Case.PutCase(id || "", data)
            .then((res) => {
                if (res.ok) {
                    setShowToast(0);
                    setCases(newCases);
                } else {
                    setShowToast(2);
                }
            })
            .catch((r) => {
                setShowToast(2);
            });
    };

    const handleCaseFormOk = (pos: number) => {
        setShowCaseForm(false);
        setShowToast(1);
        const data: NewCaseDto = {
            rule_id: id || "",
            is_active: true,
            is_archive: false,
            position: pos,
        };
        Storage.Case.PostCase(id || "", data)
            .then((res) => {
                if (res.ok) {
                    loadRule();
                    setShowToast(0);
                } else {
                    setShowToast(2);
                }
            })
            .catch((r) => {
                setShowToast(2);
            });
    };

    const handleCaseFormCancel = () => {
        setShowCaseForm(false);
    };

    const handleConditionFormSubmit = (name: string, type: string) => {
        const newCondition: NewParameterDto = {
            key: name,
            typeof: type,
        };
        const newInputs: NewParametersDto = {
            input: [newCondition],
        };

        setShowToast(1);
        setShowConditionForm(false);
        Storage.Parameter.PostCase(id || "", newInputs)
            .then((res) => {
                if (res.ok) {
                    loadRule();
                    setShowToast(0);
                } else {
                    setShowToast(2);
                }
            })
            .catch((r) => {
                setShowToast(2);
            });
    };

    const handleConditionFormCancel = () => {
        setShowConditionForm(false);
    };

    const handleKVItemFormSubmit = (name: string, type: string) => {
        const newKVitem: NewParameterDto = {
            key: name,
            typeof: type,
        };
        const newInputs: NewParametersDto = {
            output: [newKVitem],
        };

        setShowToast(1);
        setShowKVItemForm(false);
        Storage.Parameter.PostCase(id || "", newInputs)
            .then((res) => {
                if (res.ok) {
                    loadRule();
                    setShowToast(0);
                } else {
                    setShowToast(2);
                }
            })
            .catch((r) => {
                setShowToast(2);
            });
    };

    const handleKVItemFormCancel = () => {
        setShowKVItemForm(false);
    };

    // functions
    const loadRule = () => {
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
    };

    // Effects
    useEffect(() => {
        loadRule();
    }, []);

    const extraItems = [
        <ButtonGroup aria-label="Basic example">
            <Button
                size="sm"
                className="me-1"
                variant={edit ? "success" : "secondary"}
                onClick={(_) => handleUpdate()}
            >
                <i className={"bi bi-pencil me-1"} />
                {Messages.UPDATE}
            </Button>
        </ButtonGroup>,
        <ButtonGroup aria-label="Basic example">
            <Button
                name="adfas"
                size="sm"
                variant="primary"
                className="me-1"
                disabled={!edit}
                onClick={(_) => {
                    if (caseActive == "") return;

                    const caseIndex = cases.findIndex(
                        (x) => x.id == caseActive
                    );

                    if (caseIndex > 0) {
                        handleChangeCase(caseIndex, caseIndex - 1, cases);
                    }
                }}
            >
                <i className="bi bi-arrow-up"></i>
            </Button>
            <Button
                name="adfas"
                size="sm"
                variant="primary"
                className="me-1"
                disabled={!edit}
                onClick={(_) => {
                    if (caseActive == "") return;

                    const caseIndex = cases.findIndex(
                        (x) => x.id == caseActive
                    );

                    if (caseIndex >= 0) {
                        handleChangeCase(caseIndex, caseIndex + 1, cases);
                    }
                }}
            >
                <i className="bi bi-arrow-down"></i>
            </Button>
        </ButtonGroup>,

        <ButtonGroup aria-label="Basic example">
            <Button
                name="adfas"
                size="sm"
                variant="primary"
                className="me-1"
                disabled={!edit}
                onClick={(_) => {
                    if (caseActive == "") return;

                    const caseIndex = cases.findIndex(
                        (x) => x.id == caseActive
                    );

                    if (caseIndex > -1) {
                        handleActiveCase(caseIndex, cases);
                    }
                }}
            >
                <i className="bi bi-check-square"></i>
            </Button>
        </ButtonGroup>,

        <ButtonGroup aria-label="Basic example">
            <Button
                onClick={(_) => setShowCaseForm(true)}
                name="adfas"
                size="sm"
                variant="primary"
                className="me-1"
                disabled={!edit}
            >
                <i className="bi bi-plus-lg"></i> {Messages.ROW}
            </Button>

            <Button
                onClick={() => setShowConditionForm(true)}
                name="adfas"
                size="sm"
                variant="primary"
                className="me-1"
                disabled={!edit}
            >
                <i className="bi bi-plus-lg"></i> {Messages.CONDITION}
            </Button>

            <Button
                onClick={() => setShowKVItemForm(true)}
                name="adfas2"
                size="sm"
                variant="primary"
                disabled={!edit}
            >
                <i className="bi bi-plus-lg"></i> {Messages.OUTPUT}
            </Button>
        </ButtonGroup>,
    ];

    return (
        <Session>
            {showToast == 1 && <ToastWorking />}
            {showToast == 2 && <ToastError />}
            {showCaseForm && (
                <CaseForm
                    totalCases={cases.length}
                    onSubmit={handleCaseFormOk}
                    onCancel={handleCaseFormCancel}
                ></CaseForm>
            )}
            {showConditionForm && (
                <ConditionForm
                    onSubmit={handleConditionFormSubmit}
                    onCancel={handleConditionFormCancel}
                ></ConditionForm>
            )}
            {showKVItemForm && (
                <KVItemForm
                    onSubmit={handleKVItemFormSubmit}
                    onCancel={handleKVItemFormCancel}
                ></KVItemForm>
            )}
            <Menubar
                brand={Messages.NRULE}
                title={
                    (edit ? Messages.UPDATE : Messages.DISPLAY) +
                    ": " +
                    rule.name
                }
            ></Menubar>

            <Toolbar
                fluid
                title={rule.id.substring(0, 8)}
                extraItems={extraItems}
            />

            <TableEditor
                cases={cases}
                conditions={conditions}
                inputs={inputs}
                outputs={outputs}
                kvitems={kvitems}
                isUpdate={edit}
                onSelectedCase={(id) => {
                    setCaseActive(id);
                }}
            />
        </Session>
    );
}

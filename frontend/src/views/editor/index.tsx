import Session from "../../components/Session";
import Menubar from "../../components/Menubar";
import Messages from "../../locales/Messages";
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
    UpdConditionDto,
    UpdItemsConditionDto,
    UpdKVItemDto,
    UpdItemsKVItemDto,
} from "../../models";
import { Button, ButtonGroup, Container, Nav } from "react-bootstrap";
import TableEditor from "../../components/TableEditor";
import { INPUT, OUTPUT } from "../../tools";
import { ConditionDto } from "../../models/ConditionDto";
import { KVItemDto } from "../../models/KVItemDto";
import { ToastError, ToastWorking } from "../../components/Toasts";
import CaseForm from "../../components/CaseForm";
import ConditionForm from "../../components/ConditionForm";
import KVItemForm from "../../components/KVItemForm";
import Toolbar from "../../components/Toolbar";

export default function EditorView() {
    /*
     * States ---------------------------------------------------------------------
     */
    const { id } = useParams();
    const [fullscreen, setFullscreen] = useState<boolean | string>("xxl");
    const [showToast, setShowToast] = useState(0);
    const [changedConditions, setChangedConditions] = useState<ConditionDto[]>(
        []
    );
    const [changedKVItems, setChangedKVItems] = useState<KVItemDto[]>([]);
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
    /*
     * Handlers ---------------------------------------------------------------------
     */
    const handleChangeCondition = (
        variable: string,
        case_id: string,
        rule_id: string,
        operator: string,
        value: string
    ) => {
        const conditionsCopy = [...conditions];
        const idx = conditionsCopy.findIndex(
            (x) =>
                x.variable == variable &&
                x.case_id == case_id &&
                x.rule_id == rule_id
        );
        conditionsCopy[idx].operator = operator;
        conditionsCopy[idx].value = value;
        setConditions(conditionsCopy);

        const changedConditionCopy = [...changedConditions];
        const idxAux = changedConditionCopy.findIndex(
            (x) =>
                x.variable == variable &&
                x.case_id == case_id &&
                x.rule_id == rule_id
        );

        if (idxAux == -1) changedConditionCopy.push(conditionsCopy[idx]);
        else changedConditionCopy[idxAux] = conditionsCopy[idx];

        setChangedConditions(changedConditionCopy);
    };

    const handleChangeKVItem = (
        key: string,
        case_id: string,
        rule_id: string,
        value: string,
        calculation: string
    ) => {
        const kvitemsCopy = [...kvitems];
        const idx = kvitemsCopy.findIndex(
            (x) => x.key == key && x.case_id == case_id && x.rule_id == rule_id
        );
        kvitemsCopy[idx].value = value;
        kvitemsCopy[idx].calculation = calculation;
        setKVItems(kvitemsCopy);

        const changedKVItemsCopy = [...changedKVItems];
        const idxAux = changedKVItemsCopy.findIndex(
            (x) => x.key == key && x.case_id == case_id && x.rule_id == rule_id
        );

        if (idxAux == -1) changedKVItemsCopy.push(kvitemsCopy[idx]);
        else changedKVItemsCopy[idxAux] = kvitemsCopy[idx];

        setChangedKVItems(changedKVItemsCopy);
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
            })
            .finally(() => {});
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

    /*
     * Functions ---------------------------------------------------------------------
     */
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

    /*
     * Effect ---------------------------------------------------------------------
     */
    useEffect(() => {
        loadRule();
    }, []);

    const extraItems = [
        <Button
            size="sm"
            key={1}
            onClick={(_) => {
                if (
                    edit &&
                    (changedConditions.length > 0 || changedKVItems.length > 0)
                ) {
                    setShowToast(1);
                    changedConditions.map((e) => {
                        const oneCondition: UpdConditionDto = {
                            operator: e.operator,
                            value: e.value,
                            variable: e.variable,
                        };
                        const allConditions: UpdItemsConditionDto = {
                            items: [oneCondition],
                        };
                        Storage.Condition.PutCondition(
                            e.rule_id,
                            e.case_id,
                            allConditions
                        )
                            .then((res) => {
                                setShowToast(0);
                            })
                            .catch((r) => {
                                setShowToast(2);
                            })
                            .finally(() => {});
                    });

                    changedKVItems.map((e) => {
                        const onekvi: UpdKVItemDto = {
                            key: e.key,
                            value: e.value,
                            calculation: e.calculation,
                        };
                        const allkvis: UpdItemsKVItemDto = {
                            items: [onekvi],
                        };
                        Storage.KVItem.PutKVItems(e.rule_id, e.case_id, allkvis)
                            .then((res) => {
                                setShowToast(0);
                            })
                            .catch((r) => {
                                setShowToast(2);
                            })
                            .finally(() => {});
                    });

                    setEdit(!edit);
                } else {
                    setEdit(!edit);
                }
            }}
        >
            {edit ? (
                <i className="bi bi-unlock-fill"></i>
            ) : (
                <i className="bi bi-lock-fill"></i>
            )}
        </Button>,
        <ButtonGroup aria-label="Basic example">
            <Button
                className="me-1"
                size="sm"
                key={2}
                disabled={edit}
                onClick={(_) => {
                    if (caseActive == "") return;

                    const caseIndex = cases.findIndex(
                        (x) => x.id == caseActive
                    );
                    if (caseIndex > 0 && cases[caseIndex].position != 9999) {
                        handleChangeCase(caseIndex, caseIndex - 1, cases);
                    }
                }}
            >
                <i className="bi bi-arrow-up"></i>
            </Button>

            <Button
                className="me-1"
                size="sm"
                key={3}
                disabled={edit}
                onClick={(_) => {
                    if (caseActive == "") return;

                    const caseIndex = cases.findIndex(
                        (x) => x.id == caseActive
                    );
                    if (caseIndex >= 0 && caseIndex < cases.length - 2) {
                        handleChangeCase(caseIndex, caseIndex + 1, cases);
                    }
                }}
            >
                <i className="bi bi-arrow-down"></i>
            </Button>

            <Button
                size="sm"
                key={4}
                disabled={edit}
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

        <ButtonGroup>
            <Button
                className="me-1"
                size="sm"
                key={5}
                disabled={edit}
                onClick={(_) => setShowCaseForm(true)}
            >
                <i className="bi bi-plus-lg"></i> {Messages.ROW}
            </Button>

            <Button
                className="me-1"
                size="sm"
                key={6}
                disabled={edit}
                onClick={() => setShowConditionForm(true)}
            >
                <i className="bi bi-plus-lg"></i> {Messages.CONDITION}
            </Button>

            <Button
                size="sm"
                key={7}
                disabled={edit}
                onClick={() => setShowKVItemForm(true)}
            >
                <i className="bi bi-plus-lg"></i> {Messages.OUTPUT}
            </Button>
        </ButtonGroup>,

        <Button size="sm" key={8} onClick={() => setFullscreen(!fullscreen)}>
            <i className="bi bi-fullscreen"></i>
        </Button>,
    ];

    return (
        <Session>
            {showToast == 1 && <ToastWorking />}
            {showToast == 2 && <ToastError />}
            {showCaseForm && (
                <CaseForm
                    totalCases={cases.length}
                    onSubmit={handleCaseFormOk}
                    onCancel={() => setShowCaseForm(false)}
                ></CaseForm>
            )}
            {showConditionForm && (
                <ConditionForm
                    onSubmit={handleConditionFormSubmit}
                    onCancel={() => setShowConditionForm(false)}
                ></ConditionForm>
            )}
            {showKVItemForm && (
                <KVItemForm
                    onSubmit={handleKVItemFormSubmit}
                    onCancel={() => setShowKVItemForm(false)}
                ></KVItemForm>
            )}

            <Menubar
                fluid={fullscreen}
                brand={Messages.KITE}
                title={rule.name}
                extraItems={extraItems}
            />

            <Toolbar title={rule.name} extraItems={extraItems}></Toolbar>

            <Container fluid={fullscreen}>
                <TableEditor
                    cases={cases}
                    conditions={conditions}
                    inputs={inputs}
                    outputs={outputs}
                    kvitems={kvitems}
                    isEdit={!edit}
                    onSelectedCase={(id) => {
                        setCaseActive(id);
                    }}
                    onChangeCondition={handleChangeCondition}
                    onChangeKVItem={handleChangeKVItem}
                />
            </Container>
        </Session>
    );
}

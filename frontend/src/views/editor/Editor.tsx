import {
    Badge,
    Button,
    ButtonGroup,
    Col,
    Container,
    Form,
    Row,
    Table,
    ToggleButton,
} from "react-bootstrap";
import Toolbar from "../../components/Toolbar";
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { Case, ParametersDto } from "../../models";
import AddParameter from "./AddParameter";
import { Rule } from "../../typings";
import Storage from "../../storage";
import EditorToolbarButtons from "./EditorToolbarButtons";
import Messages from "../../locales/Messages";
import EditorHeader from "./EditorHeader";
import EditorSubheader from "./EditorSubheader";
import EditorRows from "./EditorRows";
import { expression } from "joi";

type Props = {};

function Editor({}: Props) {
    const { id } = useParams();
    const [conditions, setConditions] = useState<ParametersDto[]>([]);
    const [cases, setCases] = useState<Case[]>([
        {
            expressions: [
                {
                    variable: "ciclos",
                    operator: "EQ",
                    value: "2",
                },
                {
                    variable: "diasInactividad",
                    operator: "EQ",
                    value: "180",
                },
            ],
            outputs: [
                {
                    key: "tasa",
                    value: "0.15",
                },
            ],
        },
        {
            expressions: [
                {
                    variable: "ciclos",
                    operator: "EQ",
                    value: "2",
                },
                {
                    variable: "diasInactividad",
                    operator: "EQ",
                    value: "180",
                },
            ],
            outputs: [
                {
                    key: "tasa",
                    value: "0.15",
                },
            ],
        },
    ]);
    const [outputs, setOutputs] = useState<ParametersDto[]>([]);
    const [showAddParameter, setShowAddParameter] = useState(false);
    const [checked, setChecked] = useState(true);
    const [rule, setRule] = useState<Rule>({
        id: "",
        name: "",
        rule_type: "",
        strategy: "",
        version: 0,
        default_kvs: 0,
    });

    useEffect(() => {
        Storage.Rule.GetRule(id || "").then((res) => {
            res.data && setRule(res.data);
            res.data &&
                setConditions(
                    res.data!.parameters?.filter(
                        (x) => x.usefor == "CONDITION"
                    ) || []
                );
            res.data &&
                setOutputs(
                    res.data!.parameters?.filter((x) => x.usefor == "OUTPUT") ||
                        []
                );
        });
    }, []);

    return (
        <>
            {showAddParameter && (
                <AddParameter
                    title={Messages.ADDCONDITION}
                    onClose={() => setShowAddParameter(false)}
                    onAddParameter={(name, type) => console.log(name, type)}
                />
            )}

            <Toolbar
                fluid
                title="Editor"
                extraItems={[
                    EditorToolbarButtons({
                        onAddParameter: (parameter: ParametersDto) => {
                            console.log(parameter);
                            if (parameter.usefor == "CONDITION") {
                                setConditions([...conditions, parameter]);
                            } else if (parameter.usefor == "OUTPUT") {
                                setOutputs([...outputs, parameter]);
                            }
                        },
                    }),
                ]}
            ></Toolbar>

            <Container fluid>
                <Table striped bordered hover responsive size="md" style={{}}>
                    <thead>
                        <EditorHeader
                            conditions={conditions}
                            outputs={outputs}
                        ></EditorHeader>
                        <EditorSubheader
                            conditions={conditions}
                            outputs={outputs}
                        ></EditorSubheader>
                    </thead>

                    <tbody>
                        <EditorRows
                            expressions={conditions}
                            outputs={outputs}
                            cases={cases}
                        ></EditorRows>
                    </tbody>
                </Table>
            </Container>
        </>
    );
}

export default Editor;

// {outputs !== undefined &&
//     outputs!.length > 0 &&
//     outputs!
//         .filter((x) => x.usefor == "OUTPUT")
//         .map((x, idx) => (
//             <td
//                 style={{
//                     borderLeft:
//                         idx == 0
//                             ? "5px solid #49e048"
//                             : "3px solid #49e048",
//                 }}
//                 key={x.key}
//             >
//                 {idx}
//             </td>
//         ))}

// {cases !== undefined &&
//     cases!.length > 0 &&
//     cases!
//         .filter((x) => x.usefor == "CONDITION")
//         .map((x, idx) => (
//             <td
//                 style={{
//                     borderLeft:
//                         idx == 0
//                             ? "5px solid #b25afd"
//                             : "3px solid #b25afd",
//                 }}
//                 key={x.key}
//             >
//                 {idx}
//             </td>
//         ))}

// {
//     <Container>
//         <Badge bg="dark">1</Badge>
//         <ToggleButton
//             className="ms-1"
//             size="sm"
//             id="toggle-check"
//             type="checkbox"
//             variant="outline-success"
//             checked={checked}
//             value="1"
//             onChange={(e) =>
//                 setChecked(
//                     e.currentTarget.checked
//                 )
//             }
//         >
//             <i className="bi bi-check2-square"></i>
//         </ToggleButton>

//         <Button
//             className="ms-1"
//             size="sm"
//             variant="secondary"
//         >
//             <i className="bi bi-trash3"></i>
//         </Button>
//         <Button
//             className="ms-1"
//             size="sm"
//             variant="secondary"
//         >
//             <i className="bi bi-trash3"></i>
//         </Button>
//     </Container>
// }

// <Container>
//                         <ToggleButton
//                             size="sm"
//                             id="toggle-check"
//                             type="checkbox"
//                             variant="outline-success"
//                             checked={checked}
//                             value="1"
//                             onChange={(e) =>
//                                 setChecked(e.currentTarget.checked)
//                             }
//                         >
//                             <i className="bi bi-check2-square"></i>
//                         </ToggleButton>

//                         <Button className="ms-1" size="sm" variant="secondary">
//                             <i className="bi bi-trash3"></i>
//                         </Button>
//                         <Button className="ms-1" size="sm" variant="secondary">
//                             <i className="bi bi-trash3"></i>
//                         </Button>
//                     </Container>

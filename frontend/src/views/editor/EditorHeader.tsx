import Messages from "../../locales/Messages";
import { Button } from "react-bootstrap";
import { ParametersDto } from "../../models";

type Props = {
    conditions: ParametersDto[];

    outputs: ParametersDto[];
};

function EditorHeader({ conditions, outputs }: Props) {
    return (
        <tr>
            <th
                style={{
                    minWidth: "200px",
                }}
                id="actions"
            >
                Actions{" "}
                <Button
                    name="reorder"
                    className="ms-1"
                    size="sm"
                    variant="primary"
                >
                    <i className="bi bi-arrow-down-up"></i>
                </Button>
            </th>
            <th
                style={{
                    borderLeft: "5px solid #b25afd",
                    minWidth: "200px",
                }}
                colSpan={conditions?.length || 0}
                id="condition"
            >
                {Messages.EXPRESSIONS}

                <Button
                    name="reorder"
                    className="ms-1"
                    size="sm"
                    variant="primary"
                >
                    <i className="bi bi-arrow-left-right"></i>
                </Button>
            </th>
            <th
                style={{
                    borderLeft: "5px solid #49e048",
                    minWidth: "200px",
                }}
                colSpan={outputs?.length || 0}
                id="output"
            >
                {Messages.OUTPUTS}

                <Button
                    name="reorder"
                    className="ms-1"
                    size="sm"
                    variant="primary"
                >
                    <i className="bi bi-arrow-left-right"></i>
                </Button>
            </th>
        </tr>
    );
}

export default EditorHeader;

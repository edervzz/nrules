import { ParametersDto } from "../../models";

type Props = {
    conditions: ParametersDto[];
    outputs: ParametersDto[];
};

function EditorSubheader({ conditions, outputs }: Props) {
    return (
        <tr>
            <th></th>
            {conditions !== undefined &&
                conditions!.length > 0 &&
                conditions!
                    .filter((x) => x.usefor == "CONDITION")
                    .map((x, idx) => (
                        <th
                            style={{
                                borderLeft:
                                    idx == 0
                                        ? "5px solid #b25afd"
                                        : "3px solid #b25afd",
                                backgroundColor: "#e1ddfd",
                            }}
                            key={x.key}
                        >
                            {x.key} <br></br>({x.typeof})
                        </th>
                    ))}

            {outputs !== undefined &&
                outputs!.length > 0 &&
                outputs!
                    .filter((x) => x.usefor == "OUTPUT")
                    .map((x, idx) => (
                        <th
                            style={{
                                borderLeft:
                                    idx == 0
                                        ? "5px solid #49e048"
                                        : "3px solid #49e048",
                                backgroundColor: "#baffb9",
                            }}
                            key={x.key}
                        >
                            {x.key} ({x.typeof})
                        </th>
                    ))}
        </tr>
    );
}

export default EditorSubheader;

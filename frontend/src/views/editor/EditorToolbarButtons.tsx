import React, { useState } from "react";
import { Button, Container, OverlayTrigger, Tooltip } from "react-bootstrap";
import { ParametersDto } from "../../models";
import Messages from "../../locales/Messages";
import AddParameter from "./AddParameter";

type Props = {
    onAddParameter: (parameter: ParametersDto) => void;
    onAddRow: () => void;
};

const CONDITION = "CONDITION";
const OUTPUT = "OUTPUT";

const text = (showAdd: String) => {
    return showAdd == CONDITION ? Messages.ADDCONDITION : Messages.ADDOUTPUT;
};

function EditorToolbarButtons({ onAddParameter, onAddRow }: Props) {
    const [showAdd, setShowAdd] = useState("");

    return (
        <>
            {(showAdd == CONDITION || showAdd == OUTPUT) && (
                <AddParameter
                    title={text(showAdd)}
                    onClose={() => {
                        setShowAdd("");
                    }}
                    onAddParameter={(
                        name: string | undefined,
                        type: string | undefined
                    ) => {
                        onAddParameter({
                            key: name!,
                            typeof: type!,
                            usefor: showAdd,
                        });
                        setShowAdd("");
                    }}
                ></AddParameter>
            )}
            <Container>
                <Button
                    onClick={onAddRow}
                    name="adfas"
                    size="sm"
                    variant="primary"
                >
                    <i className="bi bi-plus-lg"></i> {Messages.ROW}
                </Button>

                <Button
                    onClick={() => setShowAdd("CONDITION")}
                    className="ms-3"
                    name="adfas"
                    size="sm"
                    variant="primary"
                >
                    <i className="bi bi-plus-lg"></i> {Messages.CONDITION}
                </Button>

                <Button
                    onClick={() => setShowAdd("OUTPUT")}
                    name="adfas2"
                    className="ms-1"
                    size="sm"
                    variant="primary"
                >
                    <i className="bi bi-plus-lg"></i> {Messages.OUTPUT}
                </Button>

                <Button
                    name="reorder"
                    className="ms-3"
                    size="sm"
                    variant="primary"
                >
                    <i className="bi bi-arrow-down-up"></i>
                </Button>
            </Container>
        </>
    );
}

export default EditorToolbarButtons;

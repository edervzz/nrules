import React from "react";
import { Button, Container, OverlayTrigger, Tooltip } from "react-bootstrap";
import { ParametersDto } from "../../models";
import Messages from "../../locales/Messages";

type Props = {
    onShowAddParameters: (show: boolean) => void;
    onSetCondition: (value: React.SetStateAction<ParametersDto[]>) => void;
    onSetOutputs: (value: React.SetStateAction<ParametersDto[]>) => void;
    condition: ParametersDto[];
    outputs: ParametersDto[];
};

function EditorToolbarButtons({
    onShowAddParameters,
    onSetCondition,
    onSetOutputs,
    condition,
    outputs,
}: Props) {
    return (
        <Container>
            <Button name="adfas" size="sm" variant="primary">
                <i className="bi bi-plus-lg"></i> {Messages.ROW}
            </Button>

            <Button
                onClick={() => {
                    const oneParam = {
                        key: "qwert",
                        usefor: "CONDITION",
                        typeof: "String",
                    } as ParametersDto;
                    const newParams = [...condition, { ...oneParam }];
                    onSetCondition(newParams);
                }}
                className="ms-3"
                name="adfas"
                size="sm"
                variant="primary"
            >
                <i className="bi bi-plus-lg"></i> {Messages.BUTTON_CONDITION}
            </Button>

            <Button
                name="adfas2"
                onClick={() => {
                    const oneParam = {
                        key: "zxcv",
                        usefor: "OUTPUT",
                        typeof: "String",
                    } as ParametersDto;
                    const newParams = [...outputs, { ...oneParam }];
                    onSetOutputs(newParams);
                }}
                className="ms-1"
                size="sm"
                variant="primary"
            >
                <i className="bi bi-plus-lg"></i> {Messages.BUTTON_OUTPUT}
            </Button>

            <Button name="reorder" className="ms-3" size="sm" variant="primary">
                <i className="bi bi-arrow-down-up"></i>
            </Button>
        </Container>
    );
}

export default EditorToolbarButtons;

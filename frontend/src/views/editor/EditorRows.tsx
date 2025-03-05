import {
    Badge,
    Button,
    Card,
    Col,
    Container,
    Form,
    Row,
    ToggleButton,
} from "react-bootstrap";
import { CaseDto as CaseDto, ParametersDto } from "../../models";

type Props = {
    cases: CaseDto[];
    expressions: ParametersDto[];
    outputs: ParametersDto[];
};

function EditorRows({ cases, expressions, outputs }: Props) {
    return cases.map((c, idx) => (
        <tr key={"cases" + idx}>
            <td key={"controls" + idx}>
                <Container>
                    <Badge bg="dark">1</Badge>
                    <ToggleButton
                        className="ms-1"
                        size="sm"
                        id="toggle-check"
                        type="checkbox"
                        variant="outline-success"
                        checked
                        value="1"
                    >
                        <i className="bi bi-check2-square"></i>
                    </ToggleButton>

                    <Button className="ms-1" size="sm" variant="secondary">
                        <i className="bi bi-trash3"></i>
                    </Button>
                </Container>
            </td>
            {expressions.map((e) => {
                const expression = c.conditions.filter(
                    (x) => x.variable == e.key
                );
                const oneExpression = expression.pop();
                if (oneExpression === undefined) return <></>;

                return (
                    <td key={e.key}>
                        <Container>
                            <Row
                                style={{ width: "280px" }}
                                sm="auto"
                                className="align-items-center"
                            >
                                <Button size="sm" variant="success">
                                    {oneExpression.operator}
                                </Button>
                                <Form.Control
                                    className="ms-3"
                                    size="sm"
                                    style={{ width: "200px" }}
                                    id={
                                        "input" +
                                        idx.toString() +
                                        oneExpression.variable
                                    }
                                    defaultValue={oneExpression.value}
                                />
                            </Row>
                        </Container>
                    </td>
                );
            })}
            {outputs.map((e) => {
                const out = c.kvitems.filter((x) => x.key == e.key);
                const oneOut = out.pop();
                if (oneOut === undefined) return <td></td>;
                return (
                    <td key={e.key} style={{ width: "275px" }}>
                        <Form.Control
                            className="ms-3"
                            size="sm"
                            style={{ width: "200px" }}
                            id={"input" + idx.toString() + oneOut.key}
                            defaultValue={oneOut.value}
                        />
                    </td>
                );
            })}
        </tr>
    ));
}

export default EditorRows;

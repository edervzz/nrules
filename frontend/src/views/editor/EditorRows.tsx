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
import { Case as CaseDto, ParametersDto } from "../../models";

type Props = {
    cases: CaseDto[];
    expressions: ParametersDto[];
    outputs: ParametersDto[];
};

function EditorRows({ cases, expressions, outputs }: Props) {
    return cases.map((c, idx) => (
        <tr key={idx}>
            <td key={idx}>
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
                const expression = c.expressions.filter(
                    (x) => x.variable == e.key
                );
                const oneExpression = expression.pop();
                if (oneExpression === undefined) return <td></td>;

                return (
                    <td key={e.key}>
                        <Container>
                            <Button
                                className="ms-1"
                                size="sm"
                                variant="success"
                            >
                                {oneExpression.operator}
                            </Button>
                            <Form.Control
                                id={
                                    "input" +
                                    idx.toString() +
                                    oneExpression.variable
                                }
                                value={oneExpression.value}
                            />
                        </Container>
                    </td>
                );
            })}
            {outputs.map((e) => {
                const expression = c.outputs.filter((x) => x.key == e.key);
                const oneExpression = expression.pop();
                if (oneExpression === undefined) return <td></td>;

                return <td key={e.key}></td>;
            })}
        </tr>
    ));
}

export default EditorRows;

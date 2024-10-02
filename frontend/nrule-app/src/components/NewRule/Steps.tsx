import { Button, Form, Table } from "react-bootstrap";
import Messages from "../../locales/Messages";

type Props = {
    step: Number;
};

function Steps({ step }: Props) {
    if (step == 1) {
        return (
            <Form>
                <Form.Group
                    className="mb-3"
                    controlId="exampleForm.ControlInput1"
                >
                    <Form.Label>{Messages.RULENAME}</Form.Label>
                    <Form.Control
                        placeholder="ru.domain.detail"
                        required={true}
                    />
                </Form.Group>
                <Form.Group
                    className="mb-3"
                    controlId="exampleForm.ControlInput1"
                >
                    <Form.Label>{Messages.RULETYPE}</Form.Label>
                    <Form.Select aria-label="Default select example">
                        <option>{Messages.RULETYPE_SELECT}</option>
                        <option value={1}>{Messages.TABLE}</option>
                        <option value={2}>{Messages.TREE}</option>
                    </Form.Select>
                </Form.Group>
            </Form>
        );
    }
    if (step == 2) {
        return (
            <>
                <Button size="sm">+</Button>
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Name</th>
                            <th>Type</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>Mark</td>
                            <td>Otto</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>Jacob</td>
                            <td>@fat</td>
                        </tr>
                    </tbody>
                </Table>
            </>
        );
    }
    return <div>Step1</div>;
}

export default Steps;

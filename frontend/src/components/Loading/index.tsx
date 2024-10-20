import { Button, Container, Modal, Spinner, Table } from "react-bootstrap";
import Messages from "../../locales/Messages";
import { ErrorDto } from "../../typings";

interface Props01 {
    title: string;
    isFailure: boolean;
    messageOnFailure: string;
    onClose: () => void;
}

export function Loading01({
    title,
    messageOnFailure,
    isFailure,
    onClose,
}: Props01) {
    return (
        <Modal show size="lg" backdrop="static" keyboard={false}>
            <Modal.Header>
                <Modal.Title>
                    {isFailure ? Messages.SOME_WRONG : title}
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Container className="d-flex justify-content-center">
                    {!isFailure && <Spinner animation="border" />}
                    {isFailure && `${messageOnFailure}`}
                </Container>
            </Modal.Body>
            <Modal.Footer>
                <Button disabled={!isFailure} onClick={onClose}>
                    {Messages.BUTTON_CLOSE}
                </Button>
            </Modal.Footer>
        </Modal>
    );
}

interface Props02 {
    title: string;
    isFailure: boolean;
    errorList: ErrorDto[];
    onClose: () => void;
}
export function Loading02({ title, errorList, isFailure, onClose }: Props02) {
    return (
        <Modal show size="lg" backdrop="static" keyboard={false}>
            <Modal.Header>
                <Modal.Title>
                    {isFailure ? Messages.SOME_WRONG : title}
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Container className="d-flex justify-content-center">
                    <Table>
                        <tbody>
                            {errorList.map((x) => (
                                <tr id={x.code}>
                                    <td>{x.code}</td>
                                    <td>{x.message}</td>
                                </tr>
                            ))}
                        </tbody>
                    </Table>
                </Container>
            </Modal.Body>
            <Modal.Footer>
                <Button disabled={!isFailure} onClick={onClose}>
                    {Messages.BUTTON_CLOSE}
                </Button>
            </Modal.Footer>
        </Modal>
    );
}

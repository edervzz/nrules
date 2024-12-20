import { Button, Container, Modal, Spinner, Table } from "react-bootstrap";
import Messages from "../../locales/Messages";
import { ErrorDto } from "../../models";

interface Props01 {
    show: boolean;
    title: string;
    isFailure: boolean;
    messageOnFailure: string;
    onClose: () => void;
}

export function Loading01({
    show,
    title,
    messageOnFailure,
    isFailure,
    onClose,
}: Props01) {
    return (
        <Modal show={show} size="lg" backdrop="static" keyboard={false}>
            <Modal.Header>
                <Modal.Title>
                    {isFailure ? Messages.MESSAGE_SOME_WRONG : title}
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
    show: boolean;
    title: string;
    errorList: ErrorDto[];
    isFailure: boolean;
    onClose: () => void;
}
export function Loading02({
    show,
    title,
    errorList,
    isFailure,
    onClose,
}: Props02) {
    return (
        <Modal show={show} size="lg" backdrop="static" keyboard={false}>
            <Modal.Header>
                <Modal.Title>
                    {isFailure ? Messages.MESSAGE_SOME_WRONG : title}
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Container className="d-flex justify-content-center">
                    {!isFailure && <Spinner animation="border" />}
                    {isFailure && (
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
                    )}
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

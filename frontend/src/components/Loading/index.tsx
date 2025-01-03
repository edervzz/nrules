import { Button, Container, Modal, Spinner, Table } from "react-bootstrap";
import Messages from "../../locales/Messages";
import { ErrorDto } from "../../models";

interface PropsLoading {
    show: boolean;
    title: string;
    isFailure: boolean;
    messageOnFailure: string;
    onClose: () => void;
}

export function LoadingModal({
    show,
    title,
    messageOnFailure,
    isFailure,
    onClose,
}: PropsLoading) {
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

interface PropsLoadingErrorList {
    show: boolean;
    title: string;
    errorList: ErrorDto[];
    isFailure: boolean;
    onClose: () => void;
}
export function LoadingErrorListModal({
    show,
    title,
    errorList,
    isFailure,
    onClose,
}: PropsLoadingErrorList) {
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

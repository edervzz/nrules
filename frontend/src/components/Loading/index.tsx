import { Button, Container, Modal, Spinner } from "react-bootstrap";
import Messages from "../../locales/Messages";

interface Props {
    title: string;
    messageOnFailure: string;
    isFailure: boolean;
    onClose: () => void;
}

export default function Loading01({
    title,
    messageOnFailure,
    isFailure,
    onClose,
}: Props) {
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

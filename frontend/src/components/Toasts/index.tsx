import { Toast, ToastContainer } from "react-bootstrap";
import Messages from "../../locales/Messages";

type Props = {
    delayTime?: number;
    message?: string;
};

export function ToastLoading({ delayTime = 20000 }: Props) {
    return (
        <ToastContainer position="top-center" style={{ zIndex: 1 }}>
            <Toast show={true} delay={delayTime} autohide bg="secondary">
                <Toast.Body className="text-white text-center">
                    {Messages.MESSAGE_LOADING}
                </Toast.Body>
            </Toast>
        </ToastContainer>
    );
}

export function ToastError({
    delayTime = 2000,
    message = Messages.MESSAGE_SOME_WRONG,
}: Props) {
    return (
        <ToastContainer position="top-center" style={{ zIndex: 1 }}>
            <Toast show={true} delay={delayTime} autohide bg="danger">
                <Toast.Body className="text-white text-center">
                    {message}
                </Toast.Body>
            </Toast>
        </ToastContainer>
    );
}

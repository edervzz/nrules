import { Toast, ToastContainer } from "react-bootstrap";
import Messages from "../../locales/Messages";
import { ErrorListDto } from "../../models";

type Props = {
    delayTime?: number;
    header?: string;
    message?: string;
    messages?: ErrorListDto;
    onClose?: () => void;
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

export function ToastWorking({ header = Messages.MESSAGE_WORKING }: Props) {
    return (
        <div className="toast-container top-0 start-50 translate-middle-x">
            <div className="toast text-bg-secondary show" role="alert">
                <div className="toast-header text-center">{header}</div>
                <div className="toast-body text-center"></div>
            </div>
        </div>
    );
}

export function ToastError({
    header = Messages.MESSAGE_SOME_WRONG,
    message,
    messages,
    onClose = () => {},
}: Props) {
    return (
        <div className="toast-container top-0 start-50 translate-middle-x">
            <div className="toast text-bg-danger show" role="alert">
                <div className="toast-header text-center">
                    <strong className="me-auto">{header}</strong>
                    <button
                        onClick={() => {
                            onClose();
                        }}
                        type="button"
                        className="btn-close"
                        data-bs-dismiss="toast"
                        aria-label="Close"
                    />
                </div>
                {message && <div className="toast-body">{message}</div>}
                {messages && (
                    <div className="toast-body">
                        {messages.messages?.map((x) => (
                            <div>{x.message}</div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}

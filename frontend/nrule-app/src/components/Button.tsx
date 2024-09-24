import { ReactNode } from "react";

type Props = {
    children: ReactNode;
    // isLoading: boolean;
    onClickDelegate: () => void;
};

export default function ButtonMinion({ children, onClickDelegate }: Props) {
    return (
        <button
            onClick={() => onClickDelegate()}
            type="button"
            className={"btn btn-primary"}
        >
            {children}
        </button>
    );
}

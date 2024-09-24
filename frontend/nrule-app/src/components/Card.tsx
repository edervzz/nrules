import { ReactNode } from "react";

type CardProps = {
    children: ReactNode;
};

export default function Card(props: CardProps) {
    const { children } = props;
    return (
        <div
            className="container"
            style={{
                width: "450px",
            }}
        >
            <div className="card">
                <div className="card-body">{children}</div>
            </div>
        </div>
    );
}

import { ReactNode } from "react";

type CardProps = {
    children: ReactNode;
};

export default function Card(props: CardProps) {
    const { children } = props;
    return (
        <div
            className="container"
<<<<<<< HEAD
            // style={{
            //     width: "750px",
            // }}
=======
            style={{
                width: "750px",
            }}
>>>>>>> f5be7ecff993aa42a366ac44bdf1281a0fb3934e
        >
            <div className="card">
                <div className="card-body">{children}</div>
            </div>
        </div>
    );
}

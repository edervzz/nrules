import { OperatorEnum } from "../../enums/operator";
import styles from "./OperatorTypes.module.css";

type Props = {
    operator: string;
    operText: string;
    operDescription: string;
    operEnum: OperatorEnum;
    onClickDelegate: (op: OperatorEnum) => void;
};

export default function BasicOperator({
    operator,
    operText,
    operDescription,
    operEnum,
    onClickDelegate,
}: Props) {
    const className = [`btn`, `btn-light`, `${styles.button}`].join(" ");

    const handleClick = () => {
        onClickDelegate(operEnum);
    };

    return (
        <button
            onClick={() => handleClick()}
            type="button"
            className={className}
        >
            <div className="card">
                <div className="card-body">
                    <h5 className="card-title">
                        <span className="badge text-bg-primary">
                            {operator}
                        </span>{" "}
                        {operText}
                    </h5>
                    <h6 className="card-subtitle mb-2 text-body-secondary">
                        {operDescription}
                    </h6>
                </div>
            </div>
        </button>
    );
}

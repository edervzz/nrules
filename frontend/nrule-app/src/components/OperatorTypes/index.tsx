import { OperatorEnum } from "../../enums/operator";
import styles from "./OperatorTypes.module.css";
type Props = {
    onClickDelegate: (op: OperatorEnum) => void;
};

export default function OperatorTypes({ onClickDelegate }: Props) {
    return (
        <div className="container text-center">
            <div className="row">
                <div className="col">
                    <button
                        onClick={() => onClickDelegate(OperatorEnum.EQ)}
                        type="button"
                        className={`btn btn-light ${styles.button}`}
                    >
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">= Equal</h5>
                                <h6 className="card-subtitle mb-2 text-body-secondary">
                                    Compare if value <strong>is equal</strong>{" "}
                                    to other asdfasdf asdfasdf
                                </h6>
                            </div>
                        </div>
                    </button>
                </div>
                <div className="col">
                    <button
                        onClick={() => onClickDelegate(OperatorEnum.NE)}
                        type="button"
                        className={`btn btn-light ${styles.button}`}
                    >
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">{"<> Not Equal"}</h5>
                                <h6 className="card-subtitle mb-2 text-body-secondary">
                                    Compare if value{" "}
                                    <strong>is different</strong> to other
                                </h6>
                            </div>
                        </div>
                    </button>
                </div>
            </div>

            <div className="row">
                <div className="col">
                    <button
                        onClick={() => onClickDelegate(OperatorEnum.GT)}
                        type="button"
                        className={`btn btn-light ${styles.button}`}
                    >
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">
                                    {"> Greater Than"}
                                </h5>
                                <h6 className="card-subtitle mb-2 text-body-secondary">
                                    Compare if value{" "}
                                    <strong>is greater than</strong> to other
                                </h6>
                            </div>
                        </div>
                    </button>
                </div>
                <div className="col">
                    <button
                        onClick={() => onClickDelegate(OperatorEnum.LT)}
                        type="button"
                        className={`btn btn-light ${styles.button}`}
                    >
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">{"< Less Than"}</h5>
                                <h6 className="card-subtitle mb-2 text-body-secondary">
                                    Compare if value{" "}
                                    <strong>is less than</strong> to other
                                </h6>
                            </div>
                        </div>
                    </button>
                </div>
            </div>

            <div className="row">
                <div className="col">
                    <button
                        onClick={() => onClickDelegate(OperatorEnum.GE)}
                        type="button"
                        className={`btn btn-light ${styles.button}`}
                    >
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">
                                    {">= Greater Equal"}
                                </h5>
                                <h6 className="card-subtitle mb-2 text-body-secondary">
                                    Compare if value{" "}
                                    <strong>is greater than</strong> to other
                                </h6>
                            </div>
                        </div>
                    </button>
                </div>
                <div className="col">
                    <button
                        onClick={() => onClickDelegate(OperatorEnum.LE)}
                        type="button"
                        className={`btn btn-light ${styles.button}`}
                    >
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">
                                    {"<= Less Equal"}
                                </h5>
                                <h6 className="card-subtitle mb-2 text-body-secondary">
                                    Compare if value{" "}
                                    <strong>is less than</strong> to other
                                </h6>
                            </div>
                        </div>
                    </button>
                </div>
            </div>
            <div className="row">
                <div className="col">
                    <button
                        onClick={() => onClickDelegate(OperatorEnum.IN)}
                        type="button"
                        className={`btn btn-light ${styles.button}`}
                    >
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">{"IN Into"}</h5>
                                <h6 className="card-subtitle mb-2 text-body-secondary">
                                    Compare if value{" "}
                                    <strong>is greater than</strong> to other
                                </h6>
                            </div>
                        </div>
                    </button>
                </div>
                <div className="col">
                    <button
                        onClick={() => onClickDelegate(OperatorEnum.ANY)}
                        type="button"
                        className={`btn btn-light ${styles.button}`}
                    >
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">
                                    {"NOT IN Not Into"}
                                </h5>
                                <h6 className="card-subtitle mb-2 text-body-secondary">
                                    Compare if value{" "}
                                    <strong>is less than</strong> to other
                                </h6>
                            </div>
                        </div>
                    </button>
                </div>
            </div>

            <div className="row">
                <div className="col">
                    <button
                        onClick={() => onClickDelegate(OperatorEnum.IN)}
                        type="button"
                        className={`btn btn-light ${styles.button}`}
                    >
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">{"IN Into"}</h5>
                                <h6 className="card-subtitle mb-2 text-body-secondary">
                                    Compare if value{" "}
                                    <strong>is greater than</strong> to other
                                </h6>
                            </div>
                        </div>
                    </button>
                </div>
                <div className="col">
                    <button
                        onClick={() => onClickDelegate(OperatorEnum.ANY)}
                        type="button"
                        className={`btn btn-light ${styles.button}`}
                    >
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">
                                    {"ANY Any value"}
                                </h5>
                                <h6 className="card-subtitle mb-2 text-body-secondary">
                                    Compare if value{" "}
                                    <strong>is less than</strong> to other
                                </h6>
                            </div>
                        </div>
                    </button>
                </div>
            </div>
        </div>
    );
}

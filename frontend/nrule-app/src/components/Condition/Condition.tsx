import { OperatorEnum } from "../../enums/operator";

type Props = {
    operator: OperatorEnum;
    type?: string;
};

const Condition = ({ operator }: Props) => {
    let operatorText = "";
    switch (operator) {
        case OperatorEnum.EQ:
            operatorText = "=";
            break;
        case OperatorEnum.NE:
            operatorText = "<>";
            break;
        case OperatorEnum.GT:
            operatorText = ">";
            break;
        case OperatorEnum.LT:
            operatorText = "<";
            break;
        case OperatorEnum.GE:
            operatorText = ">=";
            break;
        case OperatorEnum.LE:
            operatorText = "<=";
            break;
        case OperatorEnum.IN:
            operatorText = "IN";
            break;
        case OperatorEnum.ANY:
            operatorText = "ANY";
            break;

        default:
            break;
    }

    return (
        <div className="container">
            <button type="button" className={"btn btn-primary"}>
                {operatorText}
            </button>
            <input
                type="text"
                className="form-control"
                placeholder="Value"
                aria-label="Value"
                aria-describedby="basic-addon1"
            />
        </div>
        // <div className="container">
        //     <button type="button" className={"btn btn-primary"}>
        //         {operator}
        //     </button>
        //     <input
        //         type="text"
        //         className="form-control"
        //         placeholder="Value"
        //         aria-label="Value"
        //         aria-describedby="basic-addon1"
        //     >
        //         {value}
        //     </input>
        // </div>
    );
};

export default Condition;

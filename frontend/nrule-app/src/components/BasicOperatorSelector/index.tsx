import { OperatorEnum } from "../../enums/operator";
import BasicOperator from "../BasicOperator";
type Props = {
    onClickDelegate: (op: OperatorEnum) => void;
};

export default function BasicOperatorSelector({ onClickDelegate }: Props) {
    return (
        <div className="container text-center">
            <div className="row">
                <div className="col">
                    <BasicOperator
                        operator="EQ"
                        operText="Equal"
                        operDescription="A is equal to B"
                        operEnum={OperatorEnum.EQ}
                        onClickDelegate={onClickDelegate}
                    />
                </div>
                <div className="col">
                    <BasicOperator
                        operator="NE"
                        operText="Not Equal"
                        operDescription="A is different to B"
                        operEnum={OperatorEnum.NE}
                        onClickDelegate={onClickDelegate}
                    />
                </div>
            </div>

            <div className="row">
                <div className="col">
                    <BasicOperator
                        operator="GT"
                        operText="Greater Than"
                        operDescription="A is greater than B"
                        operEnum={OperatorEnum.GT}
                        onClickDelegate={onClickDelegate}
                    />
                </div>
                <div className="col">
                    <BasicOperator
                        operator="LT"
                        operText="Less Than"
                        operDescription="A is less than B"
                        operEnum={OperatorEnum.LT}
                        onClickDelegate={onClickDelegate}
                    />
                </div>
            </div>

            <div className="row">
                <div className="col">
                    <BasicOperator
                        operator="GE"
                        operText="Greater Equal"
                        operDescription="A is greater or equal to B"
                        operEnum={OperatorEnum.GE}
                        onClickDelegate={onClickDelegate}
                    />
                </div>
                <div className="col">
                    <BasicOperator
                        operator="LE"
                        operText="Less Equal"
                        operDescription="A is less or equal to B"
                        operEnum={OperatorEnum.LE}
                        onClickDelegate={onClickDelegate}
                    />
                </div>
            </div>
            <div className="row">
                <div className="col">
                    <BasicOperator
                        operator="IN"
                        operText="Contained"
                        operDescription="A is contained in List"
                        operEnum={OperatorEnum.IN}
                        onClickDelegate={onClickDelegate}
                    />
                </div>
                <div className="col">
                    <BasicOperator
                        operator="NOT IN"
                        operText="Not Contained"
                        operDescription="A is NOT contained in List"
                        operEnum={OperatorEnum.NI}
                        onClickDelegate={onClickDelegate}
                    />
                </div>
            </div>

            <div className="row">
                <div className="col">
                    <div className="col">
                        <BasicOperator
                            operator="BT"
                            operText="Between"
                            operDescription="A is between B and C"
                            operEnum={OperatorEnum.BT}
                            onClickDelegate={onClickDelegate}
                        />
                    </div>
                </div>
                <div className="col">
                    <BasicOperator
                        operator="ANY"
                        operText="Anything"
                        operDescription="Can be any value"
                        operEnum={OperatorEnum.ANY}
                        onClickDelegate={onClickDelegate}
                    />
                </div>
            </div>
        </div>
    );
}

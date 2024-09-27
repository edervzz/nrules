import { Button, Card, CardBody } from "react-bootstrap";
import { Operator } from "../../enums/operator";
import styles from "./OperatorTypes.module.css";

type Props = {
    operator: string;
    operText: string;
    operDescription: string;
    operEnum: Operator;
    onClickOperator: (op: Operator) => void;
};

export default function BasicOperator({
    operator,
    operText,
    operDescription,
    operEnum,
    onClickOperator,
}: Props) {
    return (
        <Button
            variant="light"
            onClick={() => onClickOperator(operEnum)}
            className={`${styles.button}`}
        >
            <Card onClick={() => onClickOperator(operEnum)}>
                <CardBody>
                    <Card.Title>
                        <span className="badge text-bg-primary">
                            {operator}
                        </span>{" "}
                        {operText}
                    </Card.Title>
                    <Card.Text>{operDescription}</Card.Text>
                </CardBody>
            </Card>
        </Button>
    );
}

import { useState } from "react";
import Condition from "./components/Condition";
import { Operator } from "./enums/operator";

function App() {
    const [operator, setOperator] = useState(Operator.EQ);

    const handleOperationSelected = (op: Operator) => {
        setOperator(op);
    };

    return (
        <Condition
            onOperationConditionSelected={handleOperationSelected}
            operator={operator}
            betweenText="&"
        ></Condition>
    );
}

export default App;

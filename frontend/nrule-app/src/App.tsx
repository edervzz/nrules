import Card from "./components/Card";
import CardBody from "./components/CardBody";
import ListHeroes, { Hero } from "./components/ListHeroes";
import ButtonMinion from "./components/Button";
import { useState } from "react";
import Condition from "./components/Condition/Condition";
<<<<<<< HEAD
import BasicOperatorSelector from "./components/BasicOperatorSelector";
=======
import OperatorTypes from "./components/OperatorTypes";
>>>>>>> f5be7ecff993aa42a366ac44bdf1281a0fb3934e
import { OperatorEnum } from "./enums/operator";

function App() {
    var list: Hero[] = [];
    list = [{ id: 1, name: "Minion", race: "Yellow" }];

    const [listMinions, setListMinions] = useState(list);

    const handleAddMinion = () => {
        setListMinions([
            ...listMinions,
            {
                id: listMinions.length + 1,
                name: "minion",
                race: "yellow",
            },
        ]);
    };

    const handleRemoveMinion = () => {
        setListMinions(listMinions.slice(0, -1));
    };

    const handleSelect = (e: Hero) => {
        console.log(e);
    };

    // renderizado condicional con short-circuit operator
    const contentListOfMonions = list.length !== 0 && (
        <ListHeroes data={listMinions} onSelectDelegate={handleSelect} />
    );

    const handleOnClickOperatorType = (op: OperatorEnum) => {
        console.log(op);
    };

    return (
        <div className="d-inline-flex p-2">
            <BasicOperatorSelector
                onClickDelegate={handleOnClickOperatorType}
            ></BasicOperatorSelector>
        </div>
    );
}

export default App;

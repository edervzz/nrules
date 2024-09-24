import Card from "./components/Card";
import CardBody from "./components/CardBody";
import ListHeroes, { Hero } from "./components/ListHeroes";
import ButtonMinion from "./components/Button";
import { useState } from "react";
import Condition from "./components/Condition/Condition";
import OperatorTypes from "./components/OperatorTypes";
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
        <Card>
            <OperatorTypes
                onClickDelegate={handleOnClickOperatorType}
            ></OperatorTypes>
            {/* <CardBody title="titulo 111" subtitle="cvbncbvn" text="ertytery " />
            <br></br>
            <ButtonMinion onClickDelegate={handleAddMinion}>
                Agregar
            </ButtonMinion>
            <ButtonMinion onClickDelegate={handleRemoveMinion}>
                Eliminar
            </ButtonMinion>
            {contentListOfMonions} */}
        </Card>
    );
}

export default App;

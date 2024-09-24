import Card from "./components/Card";
import CardBody from "./components/CardBody";
import ListHeroes, { Hero } from "./components/ListHeroes";

function App() {
    var list: Hero[];
    list = [
        { id: 1, name: "Goku" },
        { id: 2, name: "Tanjiro" },
        { id: 3, name: "Hippo" },
    ];
    return (
        <Card>
            <CardBody title="titulo 111" subtitle="cvbncbvn" text="ertytery " />
            <ListHeroes data={list} />
        </Card>
    );
}

export default App;

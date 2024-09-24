import { useState } from "react";

export type Hero = {
    id: number;
    name: string;
    race: string;
};
type ListProps = {
    data: Hero[];
    onSelectDelegate?: (h: Hero) => void;
};

// las funciones son componentes
export default function ListHeroes({ data, onSelectDelegate }: ListProps) {
    const [index, setIndex] = useState(1); // hook de estado, variable + funcion
    const handleClick = (i: number, h: Hero) => {
        setIndex(i);
        // funcion delegada
        onSelectDelegate?.(h);
    };

    return (
        <ul className="list-group">
            {data.map((e, idx) => (
                <li
                    onClick={() => handleClick(idx, e)}
                    key={e.id}
                    className={`list-group-item ${
                        index == idx ? "active" : ""
                    }`}
                >
                    {e.name}
                </li>
            ))}
        </ul>
    );
}

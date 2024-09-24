import { useState } from "react";

export type Hero = {
    id: number;
    name: string;
};
type ListProps = {
    data: Hero[];
};

// las funciones son componentes
export default function ListHeroes({ data }: ListProps) {
    const [index, SetIndex] = useState(1); // hook de estado, variable + funcion
    const handleClick = (i: number) => {
        SetIndex(i);
    };

    return (
        <ul className="list-group">
            {data.map((e, idx) => (
                <li
                    onClick={() => handleClick(idx)}
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

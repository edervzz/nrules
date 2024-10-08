import { createBrowserRouter } from "react-router-dom";
import Home from "./pages/Home";
import New from "./pages/New";
import Tables from "./pages/Tables";
import Transports from "./pages/Transports";
import Tenancy from "./pages/Tenancy";
import Users from "./pages/Users";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <Home />,
    },
    {
        path: "/new",
        element: <New />,
    },
    {
        path: "/tables",
        element: <Tables />,
    },
    {
        path: "/transports",
        element: <Transports />,
    },
    {
        path: "/tenancy",
        element: <Tenancy />,
    },
    {
        path: "/users",
        element: <Users />,
    },
]);

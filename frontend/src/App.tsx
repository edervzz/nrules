import { createBrowserRouter } from "react-router-dom";

import NewPage from "./pages/NewPage";
import TablesTage from "./pages/TablesPage";
import Transports from "./pages/TransportsPage";
import TenancyPage from "./pages/TenancyPage";
import UsersPage from "./pages/UsersPage";
import LoginPage from "./pages/LoginPage";
import HomePage from "./pages/HomePage";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <LoginPage />,
    },
    {
        path: "/home",
        element: <HomePage />,
    },
    {
        path: "/new",
        element: <NewPage />,
    },
    {
        path: "/tables",
        element: <TablesTage />,
    },
    {
        path: "/transports",
        element: <Transports />,
    },
    {
        path: "/tenancy",
        element: <TenancyPage />,
    },
    {
        path: "/users",
        element: <UsersPage />,
    },
    {
        path: "/runner",
        element: <UsersPage />,
    },
]);

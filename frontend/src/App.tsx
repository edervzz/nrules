import { createBrowserRouter } from "react-router-dom";

import NewPage from "./pages/new";
import TablesTage from "./pages/matrix";
import Transports from "./pages/TransportsPage";
import TenancyPage from "./pages/TenancyPage";
import UsersPage from "./pages/UsersPage";
import LoginPage from "./pages/login";
import HomePage from "./pages/home";

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
